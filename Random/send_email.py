import smtplib
import imghdr
from email.message import EmailMessage

value=input("Press 1 to send an email")
msg=EmailMessage()

if value=='1':
    msg['To']=input("Enter the sender's email id:")
    msg['From']=input("Enter the receiver's email id:")
    attach=input("Do you want to add any attachment?Enter Y or N")

    if attach=='Y':
        file=input('Enter full path of the file you want to upload')
        msg['Subject']="The file you wanted to send"
        msg.set_content("Please check the attached document")

        with open(file,'rb') as f:
            file_data=f.read()

        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=f.name)

    elif attach=='N':
        msg['Subject']="The text you wanted to sent"
        msg.set_content(input("Enter the text you want to sent"))

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('sohonjit.ghosh@gmail.com','footballstar')
        smtp.send_message(msg)
else:
    print('Okay, some other time')
