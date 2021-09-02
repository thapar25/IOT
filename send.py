import smtplib
import email
from email.mime.text import MIMEText
msg=MIMEText('test')
msg['Subject']="Raspi"
msg['From']=email.utils.formataddr(("pi", "pi@RasPi"))
msg["To"]=email.utils.formataddr(('Recepient','pulkit.thapar2018@vitstudent.ac.in'))
server=smtplib.SMTP("smtp.gmail.com",587)
#mail.ehlo()

mail.starttls()
mail.login('pulkit.thapar2018@vitstudent.ac.in','methapar')
mail.sendmail('pulkit.thapar2018@vitstudent.ac.in','pulkit.thapar2018@vitstudent.ac.in',value)
mail.close()
