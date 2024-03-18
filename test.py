import pickle
import numpy as np

model = pickle.load(open("model.pkl",'rb'))
# 1st index: Passenger Class
# 2nd index: Gender [0 for male, 1 for female]
# 3rd index: Age
# 4th index: No. of Sibling/Spouse on board
# 5th index: No of Parents/Children on board 
def Pclass():
    val = int(input("Enter the Passenger Class [1,2,3]: "))
    if(val==1 or val==2 or val==3):
        return val
    else:
        print("Enter the correct number in a valid range")
        Pclass()

def Gender():
    val = int(input("Enter the Gender [0 - male, 1 - female]: "))
    if(val==0 or val==1):
        return val
    else:
        print("Enter the number in a valid range")
        Gender()

def Age():
    val = int(input("Enter Age: "))
    return val

def SipSp():
    val = int(input("Enter Number of Sibling/Spouse on board: "))
    return val

def Parch():
    val = int(input("Enter Number of Parents/Children on board: "))
    return val


a = Pclass()
b = Gender()
c = Age()
d = SipSp()
e = Parch()
arr = np.array([[a,b,c,d,e]])

pred = model.predict(arr)
if(pred[0]==0):
    print("**** Survival is not Possible ****")
else:
    print("**** Survival is possible ****")

