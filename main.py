# PassGen
# These imports will be used for this project.
from colorama import Fore, Style
from colorama import init
import datetime
import string
import random
import sys
import os

# Initilaze File organizer.
os.system('title PassGen')
init(autoreset = True)

# Create Log Functions.
class LOG:
	def INFO_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"{CurrentTime} - INFO: {message}")

	def STATUS_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"{CurrentTime} - STATUS: {message}")

	def ERROR_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.RED + Style.BRIGHT + f"{CurrentTime} - ERROR: {message}")

	def WARN_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.YELLOW + Style.BRIGHT + f"{CurrentTime} - WARNING: {message}")

# This will Generate a Strong Password for the User!
def Generate(PassLen):
	JoinChars = [] # Create an Empty List.

	# Split the List of these String Operations, and Join them to JoinChars List.
	JoinChars.extend(list(string.ascii_letters))
	JoinChars.extend(list(string.digits))
	JoinChars.extend(list(string.punctuation))
	random.shuffle(JoinChars) # Shuffle the List.

	# Get the random passoword.
	return "".join(JoinChars[0:PassLen])

# Code Logic here.
LOG.WARN_LOG("Initialized PassGen!")
LOG.STATUS_LOG("Generating a Random Password for You.")

Password = Generate(random.randint(5, 17))
LOG.INFO_LOG(f"Your Password is: {Password}")
with open("Password.log", "a") as File: File.write(f"{Password}\n")
if (len(sys.argv) == 1) or (len(sys.argv) > 1 and sys.argv[1].lower() != "-o"):
	os.system("start Password.log")

sys.exit() # Exiting the program successfully.
