largest = None
smallest = None
while True:
    num1 = input("Enter a number: ")
    if num1 == "done" :   break
    try:
        num = int(num1)
    except:
        print("Invalid input")
        continue
    if smallest is None or num < smallest:
        smallest = num
        #if num < smallest:
            #smallest = num
    if largest is None or num > largest:
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)
