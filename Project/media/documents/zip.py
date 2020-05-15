import os,sys,time
from subprocess import call
from zipfile import ZipFile

def getDirectory(file):
    return os.path.dirname(os.path.abspath(file))


now=time.time()
cutoff=now - (30*86400)

cutoff1=now -(60*86400)

files=os.listdir(getDirectory(__file__))
file_path=getDirectory(__file__)


for f in files:
    if os.path.isfile(str(file_path)+f):
        stat=os.stat(str(file_path)+f)
        c=stat.st_ctime

        if c>cutoff:
            Zipobj=ZipFile('C://sample.zip','w')
            Zipobj.write(f)







