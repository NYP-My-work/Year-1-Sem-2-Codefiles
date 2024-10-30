try:
    count = int(input("How many number you want to capture? "))
    numList = []
    for i in range(count):
        msg = f"Enter number #{i+1}: "
        num = int(input(msg))
        numList.append(num)
    print(f"The lowest number in the list: {min(numList)}")
    print(f"The highest number in the list: {max(numList)}")
    print(f"The total of the number in the list: {sum(numList)}")
    print(f"The average of the number in the list: {sum(numList)/len(numList)}")
except ValueError:
    print("Inapporaprite value-- only whole numbers")
except ZeroDivisionError:
    print("No Zeros number! ")

"""
this is to get the min ,max , sum and the mean of the numbers inputed here
"""

