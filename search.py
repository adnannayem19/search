Filename = input("Enter the file name: ")
Search = input("Keyword you are searching for: ")
count = 0

fhand = open(Filename , 'r')

for line in fhand:
    if Search not in line:continue
    info = line.strip().split(":")
    count = count + 1
    print(f"\nNo: {count}")
    print(f"Full Name: {info[2]} {info[3]}")
    print(f"Phone: {info[0]}")
    print(f"Location: {info[5]} {info[6]}")
    print(f"Facebook ID: {info[1]}")
