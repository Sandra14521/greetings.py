name = input("please enter your name")
Day = input("enter the current day of the week")

print(f'Hello!{name} Happy{Day}')

feedback = input("please tell us your experience")

if not (feedback):
    print("please put a response")
else:
    print("thank you for your feedback")
