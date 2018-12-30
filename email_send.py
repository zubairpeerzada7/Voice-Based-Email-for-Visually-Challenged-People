import smtplib
def sendMail(msg='Welcome',R_mail='0',S_mail='studenttraining111@gmail.com'):
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login("studenttraining111@gmail.com", "aptron123")
   server.sendmail(S_mail,R_mail ,msg )
   server.quit()
#sendMail(R_mail='peerzubi19@gmail.com')
