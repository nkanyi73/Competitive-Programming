#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr) - 1):
            min = i
            for j in range(i,len(arr)):
                if(arr[j] < arr[min]):
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        return arr
     
