def average(array):
    # Use set to remove duplicates
    distinct_heights = set(array)
    # Calculate average
    return round(sum(distinct_heights) / len(distinct_heights), 3)

# Input reading part
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
