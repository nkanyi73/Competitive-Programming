def insertionSort1(n, arr):
    # Write your code here
    valToSort = arr[n-1]
    for i in reversed(range(0, n)):
        if arr.index(arr[i]) == 0:
                arr[0] = valToSort
                print(*arr)
        elif arr[i-1] > valToSort:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = valToSort
            print(*arr)
            break
        
