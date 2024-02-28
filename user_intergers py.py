seta = set(map(int, input("Enter the first set of int separated by spaces: ").split()))
setb = set(map(int, input("Enter the second set of int separated by spaces: ").split()))
common_elements = seta.intersection(setb)
print(f"The common elements are: {common_elements}")
