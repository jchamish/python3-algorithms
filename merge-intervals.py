
# Given a list of insurance policy intervals [(start, end), ...], write a function to merge overlapping
#  intervals and return the merged list. Optimize for time complexity.

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return merged



assert(merge_intervals([(1,3),(2,6),(8,10),(15,18)]) == [(1, 6), (8, 10), (15, 18)])