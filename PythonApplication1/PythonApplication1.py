 
import time

from win32api import GetFileVersionInfo, LOWORD, HIWORD

def get_version_number (filename):
  info = GetFileVersionInfo (filename, "\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)


def TimerHandler():
    print CheckVersion()     
    Timer()

def Timer():
    time.sleep(1)
    TimerHandler()

def CheckVersion():          
    filename =r'C:\Users\tenom\Documents\Visual Studio 2015\Projects\TPVC_App\TPVC_App\bin\Release\TPVC_App.exe' 
    return ".".join ([str (i) for i in get_version_number (filename)])

Timer()








 