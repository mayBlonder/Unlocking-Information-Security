from time import sleep, time
import sys                                  # ignore
sys.path.insert(0,'.')                      # ignore
from Root.pswd import real_password

### server side ###
def check_password(password:str) ->bool:    # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        sleep(0.1)                          # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    sleep(0.1)        
    return True
###             ###

### client side ###    
def listToString(s:list)->str:  
    str1 = "" 
    return (str1.join(s)) 
    
def test_pass(password:list)->float:  
    t_before = time()
    check_password(listToString(password))
    t_after = time()
    return (t_after - t_before)

def crack_password()->str:
    password = ['0','0','0', '0']
    digits = ('0','1','2','3','4','5','6','7','8','9')
    for i in range(4):
        for digit in digits:
            password[i] = digit
            if(test_pass(password) - ((i+2)*0.1) >= 0):
                break
    return (listToString(password))
###             ###
