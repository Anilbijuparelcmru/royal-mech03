import smtplib 
  
# list of email_id to send the mail 
li = ["anilbiju8@gmail.com", "harsharam76@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("anilbiju8@gmail.com", "anil1234") 
    message = "bro shut the hell up"
    s.sendmail("anilbiju8@gmail.com", li[i], message) 
    s.quit() 