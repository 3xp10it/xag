import os
import platform
config = os.path.expanduser("~") + "/.password"
with open(config, "r+") as f:
    _ = eval(f.read())
filename =  "xag.py"
password = _['pass']
os.system("openssl aes-256-cbc -d -in %s -out ~/.xag_tmp_file -k '%s'" %
          (filename, password))
sysinfo=platform.system()
if sysinfo=="Darwin":
    cmd="/Applications/MacVim.app/Contents/MacOS/Vim ~/.xag_tmp_file"
elif sysinfo=="Linux":
    cmd="vim  ~/.xag_tmp_file"
os.system(cmd)
os.system("openssl aes-256-cbc -in ~/.xag_tmp_file -out %s -k '%s'" %
          (filename, password))
os.system("rm ~/.xag_tmp_file")
