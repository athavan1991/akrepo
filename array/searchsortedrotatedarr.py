def findinsortrotarr(arr, num, numrotations):
    n = len(arr)

    if num > arr[n-1]:
        high = numrotations-1;
        low  = 0;
    else:
        low = numrotations;
        high = n-1;

    while(low <= high):
        mid = (low+high)/2
        if(arr[mid] == num):
            return mid
        elif num > arr[mid]:
            low = mid+1
        elif num < arr[mid]:
            high = mid-1;

    return -1;


rotatedarr = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
print findinsortrotarr(rotatedarr, 200, 6)