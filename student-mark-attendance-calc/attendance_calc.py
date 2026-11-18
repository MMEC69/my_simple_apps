while(True):
    x = input("Enter the absent days: ")
    if x == "":
        continue
    x = (30 - int(x))/30 * 100
    print(f"Attendance: {x}%\n")

