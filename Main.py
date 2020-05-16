def heapify(arr,n,i):
  largest=i
  l=i*2+1
  r=i*2+2
  if l<n and arr[l]>arr[largest]:
    largest=l
  if r<n and arr[r]>arr[largest] :
    largest=r
  if largest!=i: 
    #swap arr[largest] with arr[i]
    t=arr[largest]
    arr[largest]=arr[i]
    arr[i]=t
    heapify(arr,n,largest)  #Recursively call for affected sub tree

def buildheap(arr,n):
  s = n//2 - 1  #index of last non-leaf node 
  #Recursively heapify starting from last non-leaf node
  for i in range(s + 1):
    heapify(arr,n,s-i)
  print("After BuildHeap: ",arr)

def heapSort(arr,n):
  buildheap(arr,n)
  #one by one extract element from heap
  for i in range(n):
    #mode current root to end
    t=arr[0]
    arr[0]=arr[n-i-1]
    arr[n-i-1]=t
    #heapify the reduced heap
    heapify(arr,n-i-1,0)


print("Enter the elements to be sorted:")
a=list(map(int,input().split()))
n=len(a)
heapSort(a,n)
print("After heapsort: ",a)
