age = int(input("What is your age? "))

can_vote = True if age >= 18 else False
if can_vote:
    print("Can vote")
else:
    print("Cannot vote")
