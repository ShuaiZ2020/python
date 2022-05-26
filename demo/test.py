import time
import subprocess
cmd = [["iwr", "get.scoop.sh", -"outfile" ,"'install.ps1'"],[".\install.ps1"],["scoop",'update'], ["scoop","install", "git"], ["scoop","install","telegram","bandizip"]]
for i in cmd:
    p = subprocess.Popen(i, shell= True)
    string ,err= p.communicate()
    print(string)
    print("-------------")
