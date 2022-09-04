arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ];
n = 9;
target = 5;


def firstOccurence():
    s =0
    e = len(arr)-1
    res = -1
    while s<=e:
        mid = s + (e-s)//2

        if arr[mid] == target:
            res = mid
            s = 0
            e = mid - 1
        elif arr[mid] > target:
            
            e = mid - 1
        else:
            s = mid + 1

    return res

def lastOccurence():
    s =0
    e = len(arr)-1

    while s<=e:
        mid = s + (e-s)//2

        if arr[mid] == target:
            res = mid
            s = mid +1
            
        elif arr[mid] > target:
            
            e = mid - 1
        else:
            s = mid + 1

    return res


firstSeen = firstOccurence();
lastSeen = lastOccurence();

print([firstSeen , lastSeen])





