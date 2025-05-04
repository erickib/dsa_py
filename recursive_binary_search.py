def recursive_binary_search(list, target):
    if len(list) == 0:
        print("False: ", target, midpoint, list[midpoint])
        return False
    else:
        midpoint = (len(list)) //2

        if list[midpoint] == target:
            print("True: ", target, midpoint, list[midpoint])
            return True
        else:
            if list[midpoint] < target:
                print("if: ", target, midpoint, list[midpoint+1:])
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                print("else: ", target, midpoint, list[:midpoint])
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [x for x in range(1,9)]
indexes = [x for x in range(8)]
print("numbers ", numbers)
print("indexes ", indexes)
# result = recursive_binary_search(numbers, 8)
# verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)