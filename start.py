#! python3
# 0
#  0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
#   0              00     0  0         0           00             00       0      0    0      0   0          0
#    0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
#     0            00     0  0         0          0  0            00       0      0    0      0   0              0
#      0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
#
# authors = Monkeyboy2805
import os
import sys
import time
if sys.version_info.major != 3:
	print("Please install Python 3 to run this script.")
	time.sleep(5)
	exit(0)
sys.path.insert(0, "./project/old/lib/")
try:
	import LolexToolsMethods
except(ImportError, SyntaxError, TabError) as e:
	print(e)
	print("Missing or corrupted library. Please redownload this application or make an issue if this persists.")
	time.sleep(5)
	exit(0)
try:
	del sys.path[sys.path.index("./project/old/lib")]
except ValueError:
	pass
if LolexToolsMethods.uos.useros == "Windows":
	os.system("TITLE Lolex-Tools")
	os.system("MODE 1000")
elif LolexToolsMethods.uos.useros == "Linux" or LolexToolsMethods.uos.useros == "Android":
	sys.stdout.write("\x1b]2;Lolex-Tools\x07")
else:
	print("OS not supported!!!")
	time.sleep(5)
	exit(0)
a = input("Please enter 1 to launch the old project, 0 to launch the new project.")
if a == "1":
	os.system(LolexToolsMethods.pyo + " ./project/old/start.py")
elif a == "0":
	os.system(LolexToolsMethods.pyo + " ./project/new/start.py")
else:
	print("No such recognised version!")
