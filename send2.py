import smtplib
email = 'pulkit.thapar2018@vitstudent.ac.in'
password = 'methapar'
send_to_email = 'pulkit.thapar2018@vitstudent.ac.in' # Who you are sending the message to
message = 'test' # The message in the email

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email , message) # Send the email
server.quit() # Logout of the email server
