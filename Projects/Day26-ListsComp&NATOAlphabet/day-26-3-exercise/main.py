with open("file1.txt") as file1:
    content1 = file1.readlines()
with open("file2.txt") as file2:
    content2 = file2.readlines()

result = [int(num) for num in content1 if num in content2]

# Write your code above 👆

print(result)


