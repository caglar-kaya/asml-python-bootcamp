my_string = "*"

print("    " + my_string)
print("   " + my_string * 3)
print("  " + my_string * 5)
print(" " + my_string * 7)
print(my_string * 9)
print("   " + "||")

print("\n")

def print_a_tree(n):
    for i in range(1, n, 2):
        print(" " * int((n-i)/2) + my_string * i)
    print(" " * ((n-1) // 2) + '||')

print_a_tree(50)
