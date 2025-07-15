#  sorted array to find two numbers that add up to a target value.
def towSum(arr, target):
    left =0
    right = len(arr) -1
    while left < right:
        sum = arr[left]+ arr[right]
        if sum == target:
            return (arr[left],arr[right])
        elif sum < target:
            left += 1
        else:
            right -=1
    return None
print(towSum([1,2,3,4,5,6,7,8,9], 16 ))
