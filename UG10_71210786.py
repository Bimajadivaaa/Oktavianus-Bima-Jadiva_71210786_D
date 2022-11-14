def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56] 
lst2 = [20,21,22,23,24,25,26,27] 
lst3 = [30,29,31,33,19,20,31,21,59] 
mergesort(lst1)
mergesort(lst2)
mergesort(lst3)
print(lst1)
print(lst2)
print(lst3)
