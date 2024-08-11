from typing import List


def merge_sort(arr: List[int]):
    if len(arr) > 1:  # pass we can not divide further
        left_arr, right_arr = arr[:len(arr) // 2], arr[len(arr) // 2:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test: List[int] = [3, 4, 6, 5, 6, 2, 3, 8, 0, 1, 0, 3, 8, 2, 7, 9, 1]
merge_sort(arr_test)
print(arr_test)  # Output: [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9]
