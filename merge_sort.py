"""
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursevily sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
"""
def merge_sort(list):
    if (len(list)) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

"""
    Divide the unsorted list at midpoint into sublists
    Returns two  sublists - left and right
"""
def split(list):
    midpoint = len(list) //2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right

"""
    Merges two lists (arrays), sorting them in the process
    Returns a new merged lists
"""
def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j+=1
        
    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 62, 93, 17, 77, 31, 44, 55 ,20]
alist
l = merge_sort([54, 62, 93, 17, 77, 31, 44, 55 ,20])
print("alist ", alist)
print("sorted list ", l)
print("verify sorted alist", verify_sorted(alist))
print("verify sorted l", verify_sorted(l))
