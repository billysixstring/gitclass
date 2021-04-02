#!/usr/bin/env python3
import os
import sys

def check_reboot():
	"""Returns true if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def main():
	if (check_reboot()):
		prit("Pending Reboot")
		sys.exit(1)

main()
