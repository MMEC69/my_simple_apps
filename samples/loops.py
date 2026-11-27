exp = [2340, 2500, 2100, 3100, 2980]

total = 0

for i in range(len(exp)):
    print(f"Month: {i+1} Expense: {exp[i]}")
    total += exp[i]

print(f"Total Expense: {total}")