def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # Naive solution is to just merge the two arrays and then sort the merged array. This should probably be done using pointers, rather than merge then sort
    combined = nums1 + nums2
    for iteration in range(len(combined) -1, 0, -1):
        swapped = False
        for i in range(iteration):
            if combined[i] > combined[i+1]:
                tmp = combined[i]
                combined[i] = combined[i+1]
                combined[i+1] = tmp
                swapped = True
        if not swapped:
            break

    # Calculate the median
    if len(combined) % 2 == 0:
        return (combined[int(len(combined)/2)-1] + combined[int((len(combined)/2))])/2
    else:
        return (combined[int(len(combined)/2)])