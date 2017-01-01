import shutil, os, time, platform
init1 = time.time()
if "arm" not in platform.platform():
        exit(None)
try:
	with open ("./isnottravisci.py","a") as outf: pass
except(IOError):
	exit(None)
try:
	local = time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove folders...") 
	a = time.time()
	shutil.rmtree("./Defaults")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Defaults")
except(IOError, OSError):
	pass
try:
	a = time.time()
	shutil.rmtree("./Tests")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Tests.")
except(IOError, OSError):
	pass
try:
	local = time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove files...")
	a = time.time()
	os.remove("./LolexTools.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove LolexTools.py.")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./LolexToolsInstaller.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove LolexToolsInstaller.py")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./LolexToolsMethods.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove LolexToolsMethods.py")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./start.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove start.py")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./Androidfirsttimeinit.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Androidfirsttimeinit.py")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./busybox-armeabi")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove busybox-armeabi")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./busybox-x86")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove busybox-x86")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./Androidautoupdate.sh")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Androidautoupdate.sh")
except(IOError, OSError):
	pass
try:
	a = time.time()
	os.remove("./ver.py")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove ver.py")
except(IOError, OSError):
	pass
try:
        a = time.time()
        os.remove("./update.py")
        b = time.time()
        print("Took ",((b-a)*1000),"milliseconds to remove update.py")
except(IOError, OSError):
        pass
try:
	local = time.asctime( time.localtime(time.time()) )
	print(local, "    Copying files and folders...")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/LolexTools.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy LolexTools.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/LolexToolsInstaller.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy LolexToolsInstaller.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/LolexToolsMethods.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy LolexToolsMethods.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/start.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy start.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/Androidfirsttimeinit.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Androidfirsttimeinit.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/Androidautoupdate.sh","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Androidautoupdate.sh")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/busybox-armeabi","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy busybox-armeabi")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/busybox-x86","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy busybox-x86")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
	b = time.time()
	print("Took",((b-a)*1000),"milliseconds to copy ver.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/update.py","./")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to copy update.py")
	print("Copying folders...")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/Defaults","./Defaults")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Defaults")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/Tests","./Tests")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Tests.")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/sys","./sys")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy sys.")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/Logs","./Logs")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Logs.")
except(IOError, OSError):
	print("Please ensure that all files are present in /sdcard/Lolex-Tools")
	exit(None)
init2 = time.time()
print("Took ",((init2-init1)*1000),"milliseconds to setup Android environment")
local =time.asctime( time.localtime(time.time()) )
with open ("./androidinit.py","a") as outf:pass
print("Initialized... Starting...")

