#made by sand
import subprocess

def external_call(self,arg,shell=False):
    if shell==False:
        subprocess.call(arg)
    elif shell==True:
        subprocess.call(arg,shell=True)