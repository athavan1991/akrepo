import unittest

#merge sort
#Divide and Conquer method

#Steps
# 1. First sort the left half
# 2. Second sort the right half
# 3. Merge both the sorted arrays

def merge(arr,left,mid,right):

    #use a temp array to move the elements and then back to original arr
    temp_arr = []
    length = (right - left) + 1
    idl = mid
    idr = right

    #Two pointer technique
    #first iteratre thro both list simul
    while idl >= left and idr > mid:
        if arr[idl] >= arr[idr]:
            temp_arr.insert(0,arr[idl])
            idl -= 1
        else:
            temp_arr.insert(0, arr[idr])
            idr -= 1
    #second iterate thro remaining first array
    while idl >= left:
        temp_arr.insert(0, arr[idl])
        idl -= 1

    #third iterate thro remaining second array
    while idr > mid:
        temp_arr.insert(0, arr[idr])
        idr -= 1

    for idx in range(0, length):
        arr[left+idx] = temp_arr[idx]

    return


def mergesort(arr, left, right):
    if left >= right: 
        return       

    mid = (left + right) / 2

    mergesort(arr, left, mid)
    mergesort(arr, mid+1, right)
    merge(arr,left,mid,right)
    return arr

#call mergesort function
class firstest(unittest.TestCase):
    def test_reverse_sort(self):
        self.assertEqual(mergesort([5,4,3,2,1], 0, 4), [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()