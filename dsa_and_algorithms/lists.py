# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

print(z)

# ===========================================
p = [9, 12, 7, 4, 11]

print(p)
# Add element:
p.append(8)

print(p)
# Sort list ascending:
p.sort()

print(p)

# =======================================================
my_arr = [7, 12, 9, 4, 11, 8]
min_val = my_arr[0]

for i in my_arr:
    if i < min_val:
        min_val = i

print(f"The lowest of the given arrays: {min_val}")
# =======================================================
