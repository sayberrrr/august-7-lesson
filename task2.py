number = [1, 2, 3, 4, 5, 6,]
userEnter = input("do you want to delete  the elements? If no you can new add elements. ")

if userEnter == "yes":
    number.clear()
elif userEnter == "no":
    userElement = int(input("add new elements:"))
    number.append(userElement)

print(number)
