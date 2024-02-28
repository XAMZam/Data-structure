user_input = input("Enter a list of integers separated by spaces: ")
int = list(map(int, user_input.split()))
sum_of_int = sum(int)
print(f"The sum of the int is: {sum_of_int}")


