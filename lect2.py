name=input("please enter your name:\n").title()
course=input(f"{name} which course do you want to enroll in?:\n").upper()
website=input(f"{name} which website do you want to learn {course} from?:\n").lower()
print(f"*SUMMARY: {name} wants to learn {course} from {website}")