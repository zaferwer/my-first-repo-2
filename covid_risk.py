age = input("Are you older then 75 and cigarette addict?  (yes/no)")
chronic = input('Do you have a chronic disease? (yes/no) ')
immune = input('Do you have a weak immune system? (yes/no) ')
if age=="yes" or chronic=="yes"  or immune=="yes":
    print("You are in risky group")
else:
    print("You are not in risky group")
