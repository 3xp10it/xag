import os
import platform
from exp10it import aes_enc
from exp10it import aes_dec
config = os.path.expanduser("~") + "/.password"
with open(config, "r+") as f:
    _ = eval(f.read())
filename =  "xag.py"
password = _['pass']
with open(filename,"r+") as f:
    encstr=f.read()
message=aes_dec(encstr,password)
with open(".xag_tmp_file.py","a+") as f:
    f.write(message)
sysinfo=platform.system()
if sysinfo=="Darwin":
    cmd="/Applications/MacVim.app/Contents/MacOS/Vim .xag_tmp_file.py"
elif sysinfo=="Linux":
    cmd="vim  .xag_tmp_file.py"
os.system(cmd)
with open(".xag_tmp_file.py","r+") as f:
    message=f.read()
encstr=aes_enc(message,password)
os.system("rm xag.py")
with open("xag.py","a+") as f:
    f.write(encstr)
os.system("rm .xag_tmp_file.py")
