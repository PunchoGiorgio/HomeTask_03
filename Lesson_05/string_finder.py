filename = "rockyou.txt"
with open(filename, "rb") as file:
    contents = file.readlines()


mylist = list(str(i) for i in contents)

text = input("Enter the search text: ")

test_list = []
for i in mylist:
    if text.lower() == i[2:-3].lower():
        test_list.append(i[2:-3])
        test_list.append(i)
        break

if len(test_list):
    print(f"The searched word '{test_list[0]}' has found, at index {mylist.index(test_list[1])}")
    
elif not len(test_list):
    print("There is no such word in the list")
