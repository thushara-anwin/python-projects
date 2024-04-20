print("Welcome to my testingY quiz game!")

playing = input("Do you want to play?  ").lower()

if playing != "yes":
    quit()
print("Okay! Let's play!")
points = 0

ans = input("What does UAT stands for? "  ).lower()

if ans == "user acceptance testing":
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")
ans = input("What does SUT stands for? "  ).lower()

if (ans == "software under test"  or ans =="system under test"):
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")
ans = input("What does BDD stands for? "  ).lower()

if(ans == "behavior-driven development" or ans == "behavior driven development"):
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")

ans = input("What does CI stands for? "  ).lower()

if ans == "continuous integration":
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")

ans = input("What does CD stands for? "  ).lower()

if ans == "continuous delivery":
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")

ans = input("What does DRE stands for? "  ).lower()

if ans == "defect removal efficiency":
    print("Correct!")
    points = points+1
else:
    print("Incorrect!")
print(f"You scored {points} out of 6")
