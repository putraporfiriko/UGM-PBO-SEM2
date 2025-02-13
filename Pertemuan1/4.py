check = int(input("Enter a number: "))

#prime check logic. return 0 if not prime, 1 if prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

match isPrime(check):
    case True:
        print("Prime")
    case False:
        print("Not Prime")
    case _:
        print("wtf are you doing here. report to dev")
