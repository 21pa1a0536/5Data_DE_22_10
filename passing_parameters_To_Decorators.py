age =int(input("Enter your Age:"))
aadhar = input("Do you have Aadhar Card: type (yes/no)? ")
voterID = input("Do you have VoterID: type (yes/no)? ")

def check_voting(age):         
    def decorator(func):
        def wrapper(*args, **kwargs):
            if age >= 18:
                print("Allowed to Vote according to age")
                func(*args, *kwargs)
            else:
                print("Not Allowed to Vote according to age")
        return wrapper
    return decorator


@check_voting(age)      
def doc_check(aadhar, voterID):
    if(aadhar == "yes" and voterID == "yes"):
        print("Documents Verified: You are allowed to Vote")
    else:
        print("Documents not verified: You are not allowed to vote")


doc_check(aadhar, voterID)

