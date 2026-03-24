
import time


class FixedWindowRateLimiter:

    def __init__(self, window_size, max_requests):
        self.window_size = window_size # time will be in seconds
        self.max_requests = max_requests
        self.requests = 0
        self.window_start = time.time()
    
    def allow_request(self):
        now = time.time()

        if now - self.window_start >= self.window_size:
            self.requests = 0
            self.window_start = now
        
        if self.requests < self.max_requests:
            self.requests += 1
            return True
        return False
    

limiter = FixedWindowRateLimiter(window_size=5, max_requests=60)
print("Starting Rate Limiter Simulation..")
for i in range(1, 8):
    is_allowed = limiter.allow_request()
    
    if is_allowed:
        print("send Request")
    else:
        print("blocked")
    print(f"Request {i} | Time elapsed: ~{i * 0.5:.1f}s | Result: {is_allowed}")

    time.sleep(0.5)

