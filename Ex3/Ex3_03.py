score = float(input("Enter Score: "))

try:
    if score >= 0.9:
        print("A")
    if 0.8 <= score < 0.9:
        print("B")
    elif 0.7 <= score < 0.8:
        print("C")
    elif 0.6 <= score < 0.7:
        print("D")
    elif score < 0.6:
        print("F")
except:
    print("Error")
    score = input("Enter Score: ")
