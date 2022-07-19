import os
try:
	from BeemAfrica import Authorize, AirTime, OTP, SMS
	from configparser import ConfigParser
except:
	print("Installing Missing Dependency\n")
	os.system("pip install beem-africa > /dev/null")
	os.system("pip install requests")

cfg = ConfigParser()
cfg.read("config/config.ini")

def fuckingSetup():
	#if not cfg.get("auth", "public-key") or opt == 1:
	pub = input("Enter API-KEY/nothing for default: ")
	#if not cfg.get("auth", "private-key") or opt == 1:
	priv = input("Enter Secret-Key/nothing for default: ")
	pub = pub if len(pub) > 5 else cfg.get("auth", "public-key")
	priv = priv if len(priv) > 10 else cfg.get("auth", "private-key")
	fuckingConfig = open("config/config.ini", "w")
	fuckingData = f'[auth]\npublic-key = {pub}\nprivate-key = {priv}\n'
	fuckingConfig.write(fuckingData)
	fuckingConfig.close()

def authenticate():
	Authorize(cfg.get("auth", "public-key"), cfg.get("auth", "private-key"))
	return True

def sendSMS(target, message):
	try:
		if not target and message:
			return "ValueError"
		send = SMS.send_sms(message, target) # sender_id='sh3dyz')
		try:
			success = send['successful']
		except KeyError:
			success = None
			try:
				failed = send['code']
			except KeyError:
				failed = None
		if success:
			return send['message']
		elif failed:
			return send['message']
		else: return "UnknownError"
	except ConnectionError:
		return "Please Check Your Internet Connection"

def banner():
	#os.system("figlet beem-Africa")
	print("""
──────────────────────────────────────────────────────
─██████████████─██████──────────██████─██████████████─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████████▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████████─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████─
─██▒▒██─────────██▒▒██████▒▒██████▒▒██─██▒▒██─────────
─██▒▒██████████─██▒▒██──██▒▒██──██▒▒██─██▒▒██████████─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██████████▒▒██─██▒▒██──██████──██▒▒██─██████████▒▒██─
─────────██▒▒██─██▒▒██──────────██▒▒██─────────██▒▒██─
─██████████▒▒██─██▒▒██──────────██▒▒██─██████████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──────────██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██████████████─██████──────────██████─██████████████─
──────────────────────────────────────────────────────
""")


def main():
	# checking configuration
	key1 = cfg.get("auth", "public-key")
	key2 = cfg.get("auth", "private-key")
	if len(key1) < 5 and len(key2) < 10:
		fuckingSetup()
		os.system("bash start.sh")
	elif not authenticate():
		print("Error Invalid Keys")
	else:
		while True:
			try:
				input("\nPress Enter To Continue")
				os.system("clear")
				banner()
				target = input("Enter Target Number / 99 To Update Keys: ")
				if target == "99":
					fuckingSetup()
					continue
				message = input("Enter Message: ")
				fffffff = open('message', 'r')
				if not message:
					message = str(fffffff.read())
				if "," in target:
					target = target.split(",")
				sent = sendSMS(target, message)
				if sent == "ValueError":
					print("You Must Fill Target and Message")
				else:
					print(sent)
			except KeyboardInterrupt:
				exit("\nStoping Program")

if __name__ == "__main__":
	main()
