#! python3
import sys, time, subprocess, os, shutil, py_compile, platform, io, zipfile
try:
    import isnottravisci
except(ImportError):
    print("Please create isnottravisci.py to continue.")
    time.sleep(5)
    exit(None)
system = platform.system()
if system == "Windows":
    if sys.version_info.major != 3:
        print("Only Python 3 is currently supported. Please install Python 3.")
        time.sleep(3)
try:
    import LolexToolsMethods
except(ImportError):
    print("Missing library. Please redownload this application.")
    exit(None)
try:
    import verifonboot, LolexToolsOptions, runningsys, startplugins, theme, menusettings, restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
    system = platform.system()
    if system == "Windows":
        subprocess.Popen(".\LolexToolsInstaller.py", shell = True)
    else:
        os.system("python3 ./LolexToolsInstaller.py")
    exit(None)
if LolexToolsOptions.compiledon<9.0:
    if LolexToolsOptions.compiledon<8.3:
        shutil.copy("./update/83.py","./")
        if system == "Windows":
            if sys.version_info.minor>5:
                os.system ("py ./83.py")
            else:
                os.system("python ./83.py")
        else:
            os.system ("python3 ./83.py")
        os.remove("./83.py")
    shutil.copy("./update/90.py","./")
    if system == "Windows":
        if sys.version_info.minor>5:
            os.system ("py ./90.py")
        else:
            os.system("python ./90.py")
    else:
        os.system ("python3 ./90.py")
    os.remove("./90.py")
    print("Restarting to finish updating...")
    if system == "Windows":
        if sys.version_info.minor>5:
          os.system("py .\start.py")
        else:
           os.system("python .\start.py")
    else:
        os.system("python3 ./start.py")
    exit(None)
if system == "Windows":
    os.system(theme.theme)
    os.system("mode 1000")
print("Welcome to Lolex-Tools version 9.0exp 10:24 GMT+0.0 17/1/17")
try:
    os.system(theme.theme)
    oneswappins = verifonboot.oneswappins
    twoswappins = verifonboot.twoswappins
    runtimeone = verifonboot.runtimeone
    runtimetwo = verifonboot.runtimetwo
    oneswapwords = verifonboot.oneswapwords
    twoswapwords = verifonboot.twoswapwords
    wordtimeone = verifonboot.wordtimeone
    wordtimetwo = verifonboot.wordtimetwo
    oneuseword = LolexToolsOptions.oneuseword
    twouseword = LolexToolsOptions.twouseword
    if LolexToolsOptions.useusername == True:
        usernameenter = input("Please enter your username.")
        while usernameenter != LolexToolsOptions.username1 and usernameenter != LolexToolsOptions.username2:
            usernameenter = input("Please enter a valid username.")
    elif LolexToolsOptions.useusername == False:
        usernameenter = LolexToolsOptions.username1
    if LolexToolsOptions.username1 == usernameenter:
        if runtimeone == LolexToolsOptions.onepintotal:
            runtimeone = 1
        else:
            runtimeone = runtimeone + 1
        if LolexToolsOptions.onepintotal != 0:
            try:
                os.remove("./onepinner.py")
            except(IOError, OSError):
                pass
            with open ("./onepinner.py","a") as outf:
                outf.write("import LolexToolsOptions\npin = LolexToolsOptions.onepin")
                outf.write(str(runtimeone))
            import onepinner
            codeenter = int(input("Please enter your current PIN."))
            tries = 1
            if codeenter != onepinner.pin:
                while codeenter != onepinner.pin:
                    if tries == 5:
                        print("You got your PIN wrong 5 times.")
                        time.sleep(LolexToolsOptions.onewait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
        if verifonboot.oneswapwords == True:
            if LolexToolsOptions.onewordtotal == wordtimeone:
                wordtimeone = 1
            else:
                wordtimeone = wordtimeone + 1
            if LolexToolsOptions.onewordtotal != 0:
                try:
                    os.remove("./oneworder.py")
                except(IOError, OSError):
                	pass
                with open("./oneworder.py","a") as outf:
                    outf.write("import LolexToolsOptions\nword = LolexToolsOptions.oneword")
                    outf.write(str(wordtimeone))
                wordenter = input("Please enter your current password.")
                tries = 1
                while wordenter != oneworder.word:
                    if tries == 5:
                        print("You got your password wrong 5 times.")
                        time.sleep(LolexToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
    elif LolexToolsOptions.username2 == usernameenter:
        if runtimetwo == LolexToolsOptions.twopintotal:
            runtimetwo = 1
        else:
            runtimetwo = runtimetwo + 1
        if LolexToolsOptions.twopintotal != 0:
            try:
                os.remove("./twopinner.py")
            except(IOError, OSError):
                pass
            with open ("./twopinner.py","a") as outf:
                outf.write("import LolexToolsOptions\npin = LolexToolsOptions.twopin")
                outf.write(str(runtimetwo))
            import twopinner
            codeenter = int(input("Please enter your current PIN."))
            tries = 1
            if codeenter != twopinner.pin:
                while codeenter != twopinner.pin:
                    if tries == 5:
                        print("You got your PIN wrong 5 times.")
                        time.sleep(LolexToolsOptions.twowait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
        if verifonboot.twoswapwords == True:
            if LolexToolsOptions.twowordtotal == wordtimetwo:
                wordtimetwo = 1
            else:
                wordtimetwo = wordtimetwo + 1
            if LolexToolsOptions.twowordtotal != 0:
                try:
                	os.remove("./twoworder.py")
                except(IOError, OSError):
                    pass
                with open ("./twoworder.py","a") as outf:
                    outf.write("import LolexToolsOptions\nword = LolexToolsOptions.twoword")
                    outf.write(str(wordtimetwo))
                import twoworder
                wordenter = input("Please enter your current password.")
                tries = 1
                while wordenter != twoworder.word:
                    if tries == 5:
                        print("You got your password wrong 5 times.")
                        time.sleep(LolexToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
# This probably isn't the way to go, so I will rewrite it
# Doesn't allow for reauth on reenter while loop
# Auto generating files will probably come
# if runtimeone == 1:
#   pinneeded = LolexToolsOptions.onepin1
# if runtimeone == 1000: #Highly doubtful
#   pinneeded == ___.onepin1000
# etc etc
    if (verifonboot.runtimeone != runtimeone) or (verifonboot.runtimetwo != runtimetwo) or (verifonboot.oneswappins != oneswappins) or (verifonboot.twoswappins != twoswappins) or (verifonboot.wordtimeone != wordtimeone) or (wordtimetwo != verifonboot.wordtimetwo) or (oneswapwords != verifonboot.oneswapwords) or (twoswapwords != verifonboot.twoswapwords):
        try:
            os.remove("./verifonboot.py")
        except(IOError):
            pass
        try:
            os.remove("./verifonboot.pyc")
        except(IOError):
                print("verifonboot.pyc was not found.")
        with open ("./verifonboot.py","a") as outf:
            outf.write("oneswappins = ")
            outf.write(str(oneswappins))
            outf.write("\ntwoswappins = ")
            outf.write(str(twoswappins))
            outf.write("\nruntimeone = ")
            outf.write(str(runtimeone))
            outf.write("\nruntimetwo = ")
            outf.write(str(runtimetwo))
            outf.write("\nwordtimeone = ")
            outf.write(str(wordtimeone))
            outf.write("\nwordtimetwo = ")
            outf.write(str(wordtimetwo))
            outf.write("\noneswapwords = ")
            outf.write(str(oneswapwords))
            outf.write("\ntwoswapwords = ")
            outf.write(str(twoswapwords))
        if LolexToolsOptions.compiler == True:
            LolexToolsMethods.compiler("verifonboot")
    useros = platform.system()
    page = 0
    layout = menusettings.layout
    while True:
        modeone = "1 = Settings"
        modetwo = "2 = Restart"
        modethree = "3 = Logoff"
        modefour = "4 = Alternative Logoff Method"
        modefourlinux = "4 = Hibernate"
        modefive = "5 = Hibernate"
        modefivelinux = "5 = Shutdown"
        modesix = "6 = Shutdown"
        modesixlinux = "6 = Call A Python Shell"
        modesevenlinux = "7 = Create folders in the current location"
        modeseven = "7 = Alternative Shutdown Method"
        modeeight = "8 = Colour Flicker"
        modeeightlinux = "8 = Remove Directories"
        modenine = "9 = Call CMD"
        modeninelinux = "9 = Create files in the current location"
        modeten = "10 = Call Documents"
        modetenlinux = "10 = Restart This Script (debug purposes)"
        modeeleven = "11 = Call A Python Shell"
        modeelevenlinux = "11 = Perform Operations With Numbers"
        modetwelve = "12 = Call Task Manager"
        modetwelvelinux = "12 = Lock This Script"
        modethirteen = "13 = Create folders in the current location"
        modethirteenlinux = "13 = Start Installer"
        modefourteen = "14 = Remove Directories"
        modefourteenlinux = "14 = Show uptime and average load"
        modefifteenlinux = "15 = Dump system information into terminal"
        exitmodelinux = "16 = Exit"
        exitmodeandroid = "18 = Exit"
        modefifteen = "15 = Create files in the current location"
        modesixteen = "16 = Restart This Script (debug purposes)"
        modeseventeen = "17 = Perform Operations With Numbers"
        modeeightteen = "18 = Lock This Script"
        modenineteen = "19 = Call Remote Desktop"
        modetwenty = "20 = Call Powershell"
        modetwentyone = "21 = Print Systeminfo"
        modetwentytwo = "22 = Start Installer"
        exitmode = "23 = Exit"
        nextpage = "24 = Next Page"
        nextpageandroid= "17 = Next Page"
        backpage = "25 = Back A Page"
        backpageandroid = "18 = Back A Page"
        nextpagelinux = "17 = Next Page"
        backpagelinux = "18 = Back A Page"
        if useros != "Windows":
            if layout == 0:
                print(modeone)
                if restartsettings.hidden != True:
                    print (modetwo)
                if logoffsettings.hidden != True:
                    print (modethree)
                if useros == "Windows":
                    if logoffsettings.hidden != True:
                        print (modefour)
                    if hibernatesettings.hidden != True:
                        print(modefive)
                    if shutdownsettings.hidden != True:
                        print(modesix)
                else:
                    if hibernatesettings.hidden != True:
                        print(modefourlinux)
                    if shutdownsettings.hidden != True:
                        print(modefivelinux)
                    print(modesixlinux)
                    print(modesevenlinux)
                if useros == "Windows":
                    print (modeseven)
                    print (modeeight)
                    print (modenine)
                    print (modeten)
                    print (modeeleven)
                if useros == "Windows":
                    print (modetwelve)
                    print (modethirteen)
                    print (modefourteen)
                    print (modefifteen)
                    print(modesixteen)
                    print(modeseventeen)
                    print(modeeightteen)
                else:
                    print(modeeightlinux)
                    print(modeninelinux)
                    print(modetenlinux)
                    print(modeelevenlinux)
                    print(modetwelvelinux)
                    print(modethirteenlinux)
                    print(modefourteenlinux)
                    print(modefifteenlinux)
                    print(exitmodelinux)
                if useros == "Windows":
                    print (modenineteen)
                    print (modetwenty)
                    print (modetwentyone)
                    print(modetwentytwo)
                    print(exitmode)
            elif layout == 1:
                if page == 0:
                    print(modeone)
                    if restartsettings.hidden != True:
                        print (modetwo)
                    if logoffsettings.hidden != True:
                        print (modethree)
                    if useros == "Windows":
                        if logoffsettings.hidden != True:
                            print (modefour)
                        if hibernatesettings.hidden != True:
                            print (modefive)
                        print (nextpage)
                    else:
                        if hibernatesettings.hidden != True:
                            print(modefourlinux)
                        if shutdownsettings.hidden != True:
                            print(modefivelinux)
                        print(nextpagelinux)
                        print(backpagelinux)
                elif page == 1:
                    if useros == "Windows":
                        if shutdownsettings.hidden != True:
                            print(modesix)
                        print (modeseven)
                        print (modeeight)
                        print (modenine)
                        print (modeten)
                        print(nextpage)
                        print(backpage)
                    elif useros == "Linux":
                        page = page + 1
                if page == 2:
                    if useros == "Linux":
                        print(modesixlinux)  
                    elif useros == "Windows":
                        print(modeeleven)
                    if useros == "Linux":
                        print(modesevenlinux)
                        print(modeeightlinux)
                        print(modeninelinux)
                        print(modetenlinux)
                        print(nextpagelinux)
                        print(backpagelinux)
                    elif useros == "Windows":
                        print (modetwelve)
                        print (modethirteen)
                        print (modefourteen)
                        print (modefifteen)
                        print(nextpage)
                        print(backpage)
                elif page == 3:
                    if useros != "Linux":
                        print (modesixteen)
                        print (modeseventeen)
                        print (modeeightteen)
                    else:
                        print(modeelevenlinux)
                        print(modetwelvelinux)
                        print(modethirteenlinux)
                        print(modefourteenlinux)
                        print(modefifteenlinux)
                        print(exitmodelinux)
                    if useros == "Windows":
                        print (modenineteen)
                        print (modetwenty)
                        
                    if useros == "Windows":
                        print(nextpage)
                        print(backpage)
                    else:
                            print(nextpagelinux)
                            print(backpagelinux)
                elif page == 4:
                    if useros == "Windows":
                        print (modetwentyone)
                        print(modetwentytwo)
                        print(exitmode)
                        print(backpage)
                    else:
                        print(backpagelinux)

        if useros == "Windows":
            LolexToolsMethods.windowsnonpage(page)
        modewanted = int(input("Please enter the number of the mode that you want."))
        if useros == "Windows":
            maxmode = 26
        else:
            maxmode = 18
        while modewanted > maxmode:
            modewanted = modewanted - maxmode
        while modewanted < 1:
            modewanted = modewanted + maxmode
        if modewanted == 1:
            print("1 = Menu Settings")
            setting = int(input("Please enter the group of settings you wish to modify."))
            if setting == 1:
                    print(" Modiy Menu Layout")
                    if layout != 0:
                        print(" 0 = Default")
                    elif layout != 1:
                        print(" 1 = Pages")
                    layout = int(input("Please input the number of the setting you wish to apply."))
                    try:
                        os.remove("./menusettings.py")
                        os.remove("./menusettings.pyc")
                    except(IOError, OSError):
                        pass
                    with open ("./menusettings.py","a") as outf:
                        outf.write("layout = ")
                        outf.write(str(layout))
                    if layout = 0:
                        page = -1
            elif setting == 2:
                print("1 = Hide power menu modes.")
                settinga = int(input("Please input the number of the setting you wish to modify."))
                if settinga == 1:
                    print(modetwo, "hidden = ", restartsettings.hidden)
                    print(modethree, "hidden = ", logoffsettings.hidden)
                    print(modefourlinux, "hidden = ", hibernatesettings.hidden)
                    print(modefivelinux, "hidden = ", shutdownsettings.hidden)
                    hidestate = int(input("Please select the number of the mode."))
                    if hidestate == 2:
                        LolexToolsMethods.modehide("restart", restartsettings.hidden)
                        restartneeded = True
                    elif hidestate == 3:
                        LolexToolsMethods.modehide("logoff", logoffsettings.hidden)
                        restartneeded = True
                    elif hidestate == 4:
                        LolexToolsMethods.modehide("hibernate", hibernatesettings.hidden)
                        restartneeded = True
                    elif hidestate == 5:
                        LolexToolsMethods.modehide("shutdown", shutdownsettings.hidden)
                        restartneeded = True
                    if restartneeded == True:
                        if useros == "Windows":
                            if sys.version_info.minor>5:
                                os.system("py .\start.py")
                            else:
                                os.system("python .\start.py")
                        else:
                            os.system("python3 ./start.py")
                        exit(None)
        elif modewanted == 2:
            LolexToolsMethods.mode2()
        elif modewanted == 3:
            logoff = float(input("Please enter 1 or 0 to confirm logoff."))
            if logoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -l -f")
                else:
                    os.system("gnome-session-quit --force")
        elif modewanted == 4 and useros == "Windows" :
            altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
            if altlogoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
                time.sleep(waittime * 60)
                subprocess.Popen ("logoff.exe")
        elif (modewanted == 5 and useros == "Windows") or (modewanted == 4 and useros == "Linux"):
            hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
            if hibernate == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -h -f")
                else:
                    os.system("systemctl suspend")
        elif (modewanted == 6 and useros == "Windows") or (modewanted == 5 and useros == "Linux"):
                shutdown = int(input("Please enter 1 or 0 (no) to confirm shutdown."))
                if shutdown == 1:
                    waittime = float(input("How long, in minutes, do you wish to wait?"))
                    time.sleep (waittime * 60)
                    if useros == "Windows":
                        os.system ("shutdown -s -f")
                    elif "arm" in platform.platform()==False:
                        os.system("poweroff")
                    else:
                        if os.system("su -c reboot -p") != 0:
                            if os.system("/system/bin/reboot -p") != 0:
                                print("Failed to execute reboot binary.")
        elif modewanted == 7 and useros == "Windows" :
            altshutdown = int(input("Please enter 1 or 0 to confirm shutdown."))
            if altshutdown == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
                time.sleep (waittime * 60)
                subprocess.Popen ("shutdown.exe")
        elif modewanted == 8 and useros == "Windows" :
            LolexToolsMethods.flicker()
        elif modewanted == 9 and useros == "Windows" :
            subprocess.call("cmd.exe")
        elif modewanted == 10 and useros == "Windows" :
            subprocess.Popen("explorer.exe")
        elif (modewanted == 11 and useros == "Windows") or (modewanted == 6 and useros == "Linux"):
            if useros == "Windows":
                subprocess.call("python.exe")
            else:
                os.system("python3")
        elif modewanted == 12 and useros == "Windows" :
            subprocess.Popen("taskmgr.exe")
        elif (modewanted == 13 and useros == "Windows") or (modewanted == 7 and useros == "Linux"):
            foldername = input("Please input the name of your new folder.")
            try:
                os.makedirs (foldername)
                cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Failed to create folder: ", foldername)
        elif (modewanted == 14 and useros == "Windows") or (modewanted == 8 and useros == "Linux"):
            foldername = input("Please input the name of the folder you wish to delete.")
            try:
                 os.rmdir (foldername)
                 cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Folder does not exist!")
        elif (modewanted == 15 and useros == "Windows") or (modewanted == 9 and useros == "Linux"):
            try:
                filename = input("Please enter your file name plus the extension, eg. B.txt.  ")
                with io.FileIO (filename, "w"):
                    pass
                cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Failed to create file: ",filename)
        elif (modewanted == 16 and useros == "Windows") or (modewanted == 10 and useros == "Linux"):
            confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
            if confirmscriptrestart == 1:
                if useros == "Windows":
                    if sys.version_info.minor<6:
                        os.system("python .\start.py")
                    else:
                        os.system("py .\start.py")
                else:
                    os.system("python3 ./start.py")
                exit(None)
        elif (modewanted == 17 and useros == "Windows") or (modewanted == 11 and useros == "Linux"):
            print ("Here is a list of operations:")
            print ("1 = Add")
            print ("2 = Take")
            submode = int(input("Please enter the number of the operatino you wish to perform."))
            if submode == 1 or 2:
                startnum = int(input("Please enter your starting number."))
                addortakenum = int(input("Please input the number to be added."))
                endnum = int(input("Please enter your end number."))
                waittime = int(input("How long do you wish to wait before each operation is performed?"))
                if endnum>startnum:
                    while endnum>startnum:
                        print(startnum)
                        if addortakenum<int(0):
                            startnum = startnum - addortakenum
                        elif addortakenum > int(0):
                            startnum = startnum + addortakenum
                        time.sleep(waittime)
                    if startnum ==endnum or startnum>endnum:
                        print("The closest number to your target number was:" + (str(startnum)))
                        time.sleep (1)
                    elif startnum > endnum:
                        while startnum > endnum:
                            print (startnum)
                            if addortakenum < 0:
                                startnum = startnum + addortakenum
                            if addortakenum>0:
                                startnum = startnum = startnum - addortakenum
                                time.sleep (waittime)
                        if startnum == endnum or startnum<endnum:
                            print ("The closest number to your target end number was:" + (str(startnum)))
                            time.sleep (1)
        elif (modewanted == 18 and useros == "Windows") or (modewanted == 12 and useros == "Linux"):
            print ("Feature currently unavailable(under development).")
        elif modewanted == 19  and useros == "Windows" :
            path = input("Please input the full path of the RDP file.")
            length = len(path) - 1
            if path[length] == "p":
                length = length - 1
                if path[length] == "d":
                    length = length - 1
                    if path[length] == "r":
                        length = length - 1
                        if path[length] == ".":
                            os.system(path)
            else:
                print("Not a valid rdp file.")
        elif modewanted == 20 and useros == "Windows" :
            subprocess.call("powershell.exe")
        elif modewanted == 21 and useros == "Windows":
            os.system("systeminf")
        elif (modewanted == 22 and useros == "Windows") or (modewanted == 13 and useros == "Linux"):
            confirm = int(input("Please confirm (with a 1) to enter the installer."))
            if confirm == 1:
                if useros == "Windows":
                    if sys.version_info.minor>5:
                        os.system("py .\LolexToolsInstaller.py")
                    else:
                        os.system("python .\LolexToolsInstaller.py")
                else:
                    os.system("python3 ./LolexToolsInstaller.py")
                exit(None)
        elif (modewanted == 14 and useros == "Linux"):
            if "arm" in platform.platform():
                if os.system("/system/bin/uptime")!= 0:
                    print("Failed to run uptime script.")
            else:
                os.system("uptime")
        elif modewanted == 15 and useros == "Linux":
            if "arm" in platform.platform():
                if os.system("su -c /system/bin/dumpsys") != 0:
                    print("Cannot load as much information due to lack of root.")
                    if os.system("/system/bin/dumpsys") != 0:
                        print("Failed to execute dumpsys binary. Please check your root and SELinux statuses.")
            else:
                os.system("sudo lshw")
        elif (modewanted == 26 and useros == "Windows"):
            print("Checking for updates...")
            print("Upon prompt for saving the file, please save as Lolex-Tools-master.zip in your Lolex-Tools folder.")
            if os.system("git clone https://github.com/lolexorg/Lolex-Tools.git") != 0:
                continueto = int(input("Git was not found. Please press 1 to initiate webbrowser method or 0 to cancel."))
                if continueto == 1:
                    print("Please save your zip to Lolex-Tools newversion folder.")
                    os.system("python -m webbrowser -t https://github.com/lolexorg/Lolex-Tools/zipball/master")
                    confirm = input("Press enter to continue...")
                    try:
                        os.remove("./newversion")
                    except(IOError, OSError):
                        pass
                    os.mkdirs("./newversion")
                    newver = os.listdirs("./newversion")
                                
        # search for zips instead :P
                    zip_ref = zipfile.ZipFile("./newversion"+newver[0], "r")
                    print("Extracting...")
                    zip_ref.extractall("newversion")
                    zip_ref.close()
                    
        elif (modewanted == 24 and useros == "Windows") or (modewanted == 17 and useros == "Linux"):
            if (page < 4 and useros == "Windows") or (page < 3 and useros == "Linux"):
                page = page + 1
            else:
                page = 0
        elif (modewanted == 25 and useros == "Windows") or (modewanted == 18 and useros == "Linux"):
            if page == 2 and useros == "Linux":
                page = 0
            elif page == 3 and useros == "Linux":
                page = 1
            elif page > 0:
                page = page - 1
            else:
                if useros == "Windows":
                    page = 4
                else:
                    page = 3
        elif (modewanted == 23 and useros == "Windows") or (modewanted == 16 and useros == "Linux"):
            print("Exiting...")
            print("Giving all threads 5 seconds to exit...")
            time.sleep(5)
            os._exit(0)
except(SyntaxError):
     print("Sorry! A SyntaxError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(TypeError):
     print("Sorry! A TypeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(ValueError):
     print("Sorry! A ValueError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(IOError):
     print("Sorry! An IOError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(NameError):
     print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(EOFError):
     print("Sorry! An EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(AttributeError):
     print("Sorry! An AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(OSError):
     print("Sorry! An OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(ZeroDivisionError):
    print("Sorry! A ZeroDivisionError occured. Please do not try to divide by zero.")
