import os, platform
os.system('git pull')
 
arch = platform.architecture()[0]
if arch == "32bit":
	import EVIL32
	EVIL32.EVIL().start()
elif arch == "64bit":
	import EVIL
	EVIL.EVIL().start()
else:
	print("Something Went Wrong");