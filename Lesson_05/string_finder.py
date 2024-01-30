filename = "rockyou.txt"
with open(filename, "rb") as file:
    contents = file.readlines()


mylist = list(str(i) for i in contents)

text = input("Enter the search text: ")

test_list = []
for i in mylist:
    if text.lower() in i.lower():
        test_list.append(i)

if len(test_list):
    print(f"The searched word '{text}' has been found for {len(test_list)} times")

elif not len(test_list):
    print("There is no such word in the list")
