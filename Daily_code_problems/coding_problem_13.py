# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def lcs(s, k):
    s_idx, e_idx, m_len = 0, k, k

    while e_idx < len(s):

        e_idx += 1
        while True:
            dis_char = len(set(s[s_idx:e_idx]))
            if dis_char <= k:
                break

            s_idx += 1

        m_len = max(m_len, e_idx - s_idx)

    return m_len


print(lcs("abcba", 2))