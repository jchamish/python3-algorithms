import random

# n^2
def isEqualToK(arr, k):
    total = len(arr)
    for i in range(0, total):
        for g in range(i+1, total):
            if arr[i] + arr[g] == k:
                return True
    return False



def isEqualToKQuick(arr, k):
    vals = []
    m = int(k/2)+1
    for i in range(1, m):
        vals.append([i, k-i])

    for id, val in enumerate(vals):
        if all(item in val for item in arr):
            return True

    return False


m = []
for i in range(0, 50):
    m.append(random.randint(0,100))

m.sort()

print(isEqualToK(m, random.randint(0,100)))
print(isEqualToKQuick(m, random.randint(0,100)))
print(isEqualToKQuick(m, random.randint(0,100)))