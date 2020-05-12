from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from MoveFiles.forms import DocumentsForm
from MoveFiles.models import Documents

import os
import subprocess
from subprocess import Popen,PIPE,STDOUT
import paramiko



# Create your views here.
def upload(request):
    if  request.method == "POST":
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list')
            except:
                pass
    else:
        form=DocumentsForm()
        return render(request,"upload.html",{'form': form})


def list(request):
    document=Documents.objects.all()
    return render(request,"list.html",{'doc':document})


def delete(request,id):
    doc=Documents.objects.get(id=id)
    doc.delete()
    return redirect('/list')


def execute(request,id):
    doc = Documents.objects.get(id=id)
    path = doc.document.path
    p=os.path.basename(path)

    pa=os.path.join("media\documents",p)
    print(pa)
    print(p)
    print (path)
    loc='/home/vagrant/scripts/{}'.format(p)
    cmd = " cd /home/vagrant/scripts; python {}".format(p)
    
    
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

    ftp_client=p.open_sftp()
    print('/home/vagrant/scripts/{}'.format(p))
    # ftp_client.put( pa,'/home/vagrant/scripts/{}'.format(p))
    ftp_client.put( pa,loc)
    ftp_client.close()
    try:
        
        #cmd = " cd /home/vagrant/scripts; python first.py"
        stdin,stdout,stderr=p.exec_command(cmd)
        op=stdout.readlines()
        op=" ".join(op)
        print(op)
        result = {"status":"Success","output":str(op)}
       
    except Exception as e:
        result = {"status":"Failed","output":str(e)}

    return render(request,"result.html",{'res':result})





    