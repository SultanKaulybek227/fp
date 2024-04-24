def generate_permutations(arr):
    if len(arr) == 1:
        yield arr
    else:
        for i in range(len(arr)):
            first_element = arr[i]
            remaining_elements = arr[:i] + arr[i+1:]
            for perm in generate_permutations(remaining_elements):
                yield [first_element] + perm

my_list = [5, 9, 4, 3]
for permutation in generate_permutations(my_list):
    print(permutation)
