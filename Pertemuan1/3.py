niu = int(input("Enter your identification number: "))
if len(str(niu)) != 6: #there aren't any firm guide to what dtype the niu should be
    print("Invalid identification number")
    exit()
assignmentScore = int(input("Enter your assignment score: "))
reportScore = int(input("Enter your report score: "))

avg = (assignmentScore + reportScore) / 2
match avg:
    case _ if avg < 40:
        print("Fail")
        exit()
    case _:
        pass

examScore = int(input("Enter your exam score: "))

finalScore = (assignmentScore/2 + reportScore/2 + examScore)/2

match finalScore:
    case _ if 80<=finalScore<=100:
        print("A")
    case _ if 70<=finalScore<80:
        print("B")
    case _ if 60<=finalScore<70:
        print("C")
    case _ if 50<=finalScore<60:
        print("D")
    case _:
        print("E")
