#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import sys
sys.path.insert(0, "./ci/lib/")
import LolexToolsCIlib
del sys.path[sys.path.index("./ci/lib/")]
sys.path.insert(0, "./ci/build/prop/")
import LATEST_PYTHON_VERSION
del sys.path[sys.path.index("./ci/build/prop/")]
LolexToolsCIlib.update_py_ver()
if int(LATEST_PYTHON_VERSION.version) == int(LolexToolsCIlib.get_py_ver()):
    LolexToolsCIlib.update_py_ver()
    LolexToolsCIlib.update_headers()
else:
    exit(0)
