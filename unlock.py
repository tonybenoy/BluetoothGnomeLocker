from bluetooth import *
import subprocess
i = 0
while(True):
    dev = []  # add device mac address as a list
    lookup = []
    for item in dev:
        a = lookup_name(item)
        if (a != None):
            lookup.append(a)
    if lookup!=[] and i == 1:
        bashCommand = "loginctl unlock-session"
        subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        i=0
    elif  lookup==[] and i == 0:
        bashCommand = "dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock"
        subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        i=1