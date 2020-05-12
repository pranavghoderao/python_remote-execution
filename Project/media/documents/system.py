import subprocess

def one():

     uname="uname"
     uname_arg="-a"
     subprocess.call([uname,uname_arg])

def disk():
    diskspace="df"
    disk_arg="-hs"
    subprocess.call([diskspace,disk_arg])


def tem_disk():
    disksp="du"
    disk_agr="-hs"
    subprocess.call([disksp.disk_arg])


one()
disk()
tem_disk()

