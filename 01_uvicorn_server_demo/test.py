# 快速排序的Python实现
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 将数组分成两半
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 递归排序两半
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 合并两个有序数组
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 比较两个数组的元素并合并
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余的元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_in_place(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        print(f"low: {low}, high: {high}")

        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)
    
    return arr

# Example usage:
if __name__ == "__main__":
    # Test the functional version
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = quick_sort(test_arr1)
    print("Functional quicksort result:", sorted_arr1)
    
    # Test the in-place version
    test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    quick_sort_in_place(test_arr2)
    print("In-pl`ace quicksort result:", test_arr2)

    test_arr3 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr3 = merge_sort(test_arr3)
    print("Merge sort result:", sorted_arr3)

    merge_sort_in_place(test_arr3)
    print("Merge sort in place result:", test_arr3)
    
