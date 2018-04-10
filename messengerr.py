import smtplib
import time
import random

server = smtplib.SMTP('smtp.gmail.com' , 587)

server.ehlo()
server.starttls()
msg = "Check your school email."

emails = [
		"itzzaspammr@gmail.com",
		"spammin.n.hammin@gmail.com", 
		"remmapsami@gmail.com"
		]

passwords = {
	"itzzaspammr@gmail.com" : "SPAMmmmm",
	"spammin.n.hammin@gmail.com" : "SPAMmmmm",
	"remmapsami@gmail.com" : "SPAMmmmm"
}
while True:
	email = random.choice(emails)
	server.login(email, passwords[email])


	server.sendmail(email, "4438086709@vtext.com", msg)
	print("Sent " + msg + " from " + email + ".")
	time.sleep(1)


# Verizon = vtext.com
# Ting = message.ting.com or idk ting doesnt work
# ^ = maybe tmomail.net
# AT&T = txt.att.net