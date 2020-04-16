def merge(arr_a, arr_b):
    # print('\n---- start of merge ----')
    merged_arr = []

    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0].value < arr_b[0].value:
            # print('merged_arr:', merged_arr, '-- low:', arr_a, '-- high', arr_b)
            merged_arr.append(arr_a[0])
            arr_a.pop(0)
        else:
            # print('merged_arr:', merged_arr, '-- low:', arr_a, '-- high: ', arr_b)
            merged_arr.append(arr_b[0])
            arr_b.pop(0)
    remainder = arr_b if not len(arr_a) else arr_a
    while len(remainder):
        # print('merged_arr:', merged_arr, '-- remainder:', remainder)
        merged_arr.append(remainder[0])
        remainder.pop(0)
    print('\n')
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # print('mid:', mid, '-- low:', arr[:mid], '-- high:', arr[mid:])
    recursive_low = merge_sort(arr[:mid])
    recursive_high = merge_sort(arr[mid:])
    return merge(recursive_low, recursive_high)


# test_arr = [[1, 42, 81], [2, 42, 42],
#             [3, 68, 56], [4, 68, 25],
#             [5, 77, 14], [6, 57, 63],
#             [7, 17, 75], [8, 19, 41],
#             [9, 94, 19], [10, 34, 12]]
# print('Starting point:', test_arr, '\nFinal result:  ', merge_sort(test_arr))
