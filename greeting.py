name = input("please enter your name")
Day = input("enter the current day of the week")

print(f'Hello!{name} Happy{Day} enjoy your day')

# feedback


def get_feedback():
    feedback = input("how was your experience?")
    print("thank you for your feedback.")
    get_feedback()
