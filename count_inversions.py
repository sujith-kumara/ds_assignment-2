def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_inversions = count_inversions(arr[:mid])
    right_half, right_inversions = count_inversions(arr[mid:])
    merged_arr, split_inversions = merge_and_count_split_inversions(left_half, right_half)

    total_inversions = left_inversions + right_inversions + split_inversions

    return merged_arr, total_inversions

def merge_and_count_split_inversions(left, right):
    result = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversions

# Example usage
arr = [7, 5, 3, 1, 8, 6, 4, 2]
sorted_arr, inversions = count_inversions(arr)
print("Sorted Array:", sorted_arr)
print("Number of Inversions:", inversions)
