import subprocess
from ctypes import windll

SHERB_NOCONFIRMATION = 1
SHERB_NOPROGRESSUI = 2
SHERB_NOSOUND = 4
EWX_LOGOFF = 0x00000000
CREATE_NO_WINDOW = 0x08000000


def shell_open(location):
    subprocess.call(["cmd", "/c", "start", location], creationflags=CREATE_NO_WINDOW)


# System
def empty_recycling_bin():
    windll.shell32.SHEmptyRecycleBinA(None, None, SHERB_NOCONFIRMATION)


def lock():
    windll.user32.LockWorkStation()


def logout():
    windll.user32.ExitWindowsEx(EWX_LOGOFF, 1)


def restart():
    subprocess.call(["shutdown.exe", "-r", "-t", "0"], creationflags=CREATE_NO_WINDOW)


def sleep():
    windll.PowrProf.SetSuspendState(0, 1, 0)


def hibernate():
    windll.PowrProf.SetSuspendState(1, 1, 0)


def shutdown():
    subprocess.call(["shutdown.exe", "-s", "-t", "0"], creationflags=CREATE_NO_WINDOW)


# Shell
def open_recycling_bin():
    shell_open("shell:RecycleBinFolder")