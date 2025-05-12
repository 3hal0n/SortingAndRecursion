def insertionSort(A):
    for j in range(1, len(A)):
        key=A[j]
        i=j-1

        while(i>-1 and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
        
def findMedian(A):
    if(len(A)%2==0):
        return (A[len(A)//2] + A[len(A)//2 -1]) /2
    
    else:
        return A[len(A)//2]

def findRange(A):
    return A[-1]-A[0]
     

A=[]
print("Enter marks: ")
for i in range(9):
    m=int(input(": "))
    A.append(m)

insertionSort(A)
print("After sorting: ",A)


median=findMedian(A)
valRange=findRange(A)


print("Median: ",median)
print("Range: ",valRange)
