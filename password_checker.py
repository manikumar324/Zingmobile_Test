import re
class PasswordChecker:
    def __init__(self):
        self.password=input()
    def is_safe_or_not(self):
        if(len(self.password)<8):
            return False
        if(not re.search("[a-z]",self.password)):
            return False
        if(not re.search("[A-Z]",self.password)):
            return False
        if(not re.search("[0-9]",self.password)):
            return False
        if(not re.search("[_@$]",self.password)):
            return False
        return True
    
app=PasswordChecker()
if(app.is_safe_or_not()):
    print("Password is safe")
else:
    print("Password is not safe")
        