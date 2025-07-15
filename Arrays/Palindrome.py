def isPalindrome(arr):
    left =0
    right = len(arr) -1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -=1
    return True

print(isPalindrome([1,2,3,3,2,1]))