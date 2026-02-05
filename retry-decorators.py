import functools

def retry(n: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
            if last_exception:
                raise last_exception
            raise RuntimeError(f"Failed to execute {func.__name__} after {n} retries")
        return wrapper
    return decorator


import unittest


class TestRetryDecorator(unittest.TestCase):

    def test_succeeds_first_try(self):
        call_count = 0

        @retry(3)
        def succeed():
            nonlocal call_count
            call_count += 1
            return "ok"

        result = succeed()
        self.assertEqual(result, "ok")
        self.assertEqual(call_count, 1)

    def test_succeeds_after_failures(self):
        call_count = 0

        @retry(3)
        def fail_then_succeed():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("not yet")
            return "ok"

        result = fail_then_succeed()
        self.assertEqual(result, "ok")
        self.assertEqual(call_count, 3)

    def test_raises_after_all_retries_exhausted(self):
        call_count = 0

        @retry(3)
        def always_fail():
            nonlocal call_count
            call_count += 1
            raise RuntimeError("boom")

        with self.assertRaises(RuntimeError) as ctx:
            always_fail()
        self.assertEqual(str(ctx.exception), "boom")
        self.assertEqual(call_count, 3)

    def test_preserves_function_name(self):
        @retry(2)
        def my_function():
            pass

        self.assertEqual(my_function.__name__, "my_function")

    def test_passes_args_and_kwargs(self):
        @retry(2)
        def add(a, b, extra=0):
            return a + b + extra

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 2, extra=10), 13)

    def test_retry_one_means_single_attempt(self):
        call_count = 0

        @retry(1)
        def fail_once():
            nonlocal call_count
            call_count += 1
            raise ValueError("fail")

        with self.assertRaises(ValueError):
            fail_once()
        self.assertEqual(call_count, 1)

    def test_raises_last_exception_not_first(self):
        call_count = 0

        @retry(3)
        def different_errors():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise ValueError("first")
            elif call_count == 2:
                raise TypeError("second")
            else:
                raise RuntimeError("third")

        with self.assertRaises(RuntimeError) as ctx:
            different_errors()
        self.assertEqual(str(ctx.exception), "third")


if __name__ == "__main__":
    unittest.main()

