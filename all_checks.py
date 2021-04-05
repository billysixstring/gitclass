#!/usr/bin/env python3
import os
import sys
import socket

def check_reboot():
	"""Returns true if the computer has a pending reboot. Added more to this comment from GitHub."""
	return os.path.exists("/run/reboot-required")

def check_no_network():
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks=[
		(check_reboot, "Pending reboot"),
		(check_no_network, "No working network")
	]

	everything_ok=True

	for check, msg in checks:
		if check():
			print(msg)
			everything_ok=False

	if not everything_ok:
		sys.exit(1)

	print("Everything is ok, so don't worry.")
	sys.exit(0)
main()
