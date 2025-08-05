import itertools

data = input("enter character")
permute = list(itertools.permutations(data))
print("Permutations of the given data:")
for i in permute:
    print(''.join(i))