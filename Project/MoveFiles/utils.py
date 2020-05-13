from MoveFiles.models import Documents

import paramiko
import os

class connectServer():

    def connect(self):
        p= paramiko.SSHClient()
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ip= "192.168.147.10"
        uname= "vagrant"
        #passd= "vagrant"
        try:
            p.connect(ip,port=22,username=uname,key_filename='C:\\Users\\pghoderao\\Downloads\\key\\private_key_open_ssh')
        except:
            print("[!] Cannot connect to the SSH Server")
            exit()

        return p

    def loadScript(self,id,par):
        doc = Documents.objects.get(id=id)
        path = doc.document.path
        p=os.path.basename(path)

        pa=os.path.join("media\documents",p)
        print(pa)
        print(p)
        print (path)
        loc='/home/vagrant/scripts/{}'.format(p)

        ftp_client=par.open_sftp()
        print('/home/vagrant/scripts/{}'.format(p))
        
        ftp_client.put( pa,loc)
        ftp_client.close()

        return p