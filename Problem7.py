# finding the second largest number in a list
numbers = list(map(int, input("Enter numbers: ").split()))
numbers = set(numbers)
numbers=list(numbers)
numbers.sort()
if len(numbers) > 1:
    print("Second largest number:", numbers[-2])
else:
    print("Second largest number: Not available")