import random
from firebase import firebase
import smtplib

url='https://monitoring-of-turbidity.firebaseio.com/' 
firebase = firebase.FirebaseApplication(url)
print("Random integer from 0 to 100")
num2 = random.randint(0, 100)
result=firebase.put('/sensor value','random value', num2)
print(result) 


# Your gmail Credentials 
username =  input("type email adddress and press enter: ")
password = input("Type your password and press enter: ")

#this is your list of email addresses to which email has to be sent. 
input_string = input("Enter email addresses separated by space ")
print("\n")
addresslist = input_string.split()
print("now, check your gmail account !")

 
for address in addresslist: 
    toaddrs  = address
    fromaddr = 'username' 
    TEXT = 'The sensor value exceed from 30' 
    SUBJECT = 'INFO REGARDING TURBIDITY' 
    msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT) 
 
    
    # Sending the mail
    if result>30:
        server = smtplib.SMTP('smtp.gmail.com',587) 
        server.starttls() 
        server.login(username,password) 
        server.sendmail(fromaddr, toaddrs, msg) 
        server.quit() 
