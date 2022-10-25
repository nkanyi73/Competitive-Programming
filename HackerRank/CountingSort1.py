def countingSort(arr):
    # Write your code here
    counter = [0] * 100
    for i in arr:
        counter[i] += 1
    return counter
