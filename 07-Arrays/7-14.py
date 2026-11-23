def bubbleSort(arr):
   n = len(arr)
   for i in range(0, n - 1):
      for j in range(0, n-i-2):
         if arr[j] > arr[j+1]:
               x = arr[j]
               arr[j] = arr[j+1]
               arr[j+1] = x
   return arr

print(bubbleSort([2,5,2,1,6,7,2,5]))

#źle