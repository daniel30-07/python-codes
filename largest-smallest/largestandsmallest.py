# This program reapetedly prompts a user for integer numbers and print out the Largest and the Smallest number. As well the program don't aceept strings or invalid numbers


largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        num = float(num)
        if largest is None :
            largest = num
        if smallest is None :
            smallest = num
        if num > largest :
            largest = num
        if num < smallest :
            smallest = num
    except :
        print('Invalid input')


print("Maximum is", int(largest))
print("Minimum is", int(smallest))
