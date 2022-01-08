"""
Write a function called sumIntervals/sum_intervals() that accepts an array of
 intervals, and returns the sum of all the interval lengths. 
 Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. 
The first value of the interval will always be less than the second value. 
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
"""

def sum_of_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    total = 0 
    
    interval_arr = []

    for i in range(len(sorted_intervals)):
        interval = sorted_intervals[i]
        if not interval_arr:
            interval_arr.extend(list(interval))
        
        elif interval[0] < interval_arr[-1]:
            interval_arr.extend(list(interval))
            interval_arr.sort()

        else:
            total += interval_arr[-1] - interval_arr[0]
            interval_arr = list(interval)

        if i + 1 == len(sorted_intervals):
            total += interval_arr[-1] - interval_arr[0]

    return total


if __name__ == '__main__':
    print(sum_of_intervals([(1, 5)]), 4)
    print(sum_of_intervals([(1, 5), (6, 10)]), 8)
    print(sum_of_intervals([(1, 5), (1, 5)]), 4)
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)