from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from MoveFiles.forms import DocumentsForm
from MoveFiles.models import Documents
from MoveFiles.utils import connectServer
from MoveFiles.run_script import execution

import os

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
    util = connectServer()
    ex = execution()

    par = util.connect()
    p = util.loadScript(id,par)

    ext = os.path.splitext(p)
    print(ext[1])
    if (ext[1] == ".py"):
        rest =  ex.runScriptPython(id,par,p)
    if (ext[1] == ".sh"):
        rest = ex.runScriptShell(id,par,p)

    
    return render(request,"result.html",{'res':rest})

def remoterun(request):
    ex = execution()
    util = connectServer()
    par = util.connect()
    filenames = ex.getFileNames(par)
    return render(request,"remote.html",{'fnames':filenames})


def run(request):
    if request.method == "POST":
        script_name = request.POST.get('scriptname')
        print(script_name)
        
        util = connectServer()
        par = util.connect()
        ex = execution()
        filenames = ex.getFileNames(par)
        
        if script_name in filenames:
            loc = "/home/vagrant/scripts/"
            ext = os.path.splitext(script_name)
            print(ext[1])
            if (ext[1] == ".py"):
                rest =  ex.remoteRunPython(loc,script_name,par)
            if (ext[1] == ".sh"):
                rest = ex.remoteRunShell(loc,script_name,par)

            return render(request,"result.html",{'res':rest})
    
        restf={"status":"failed..","output":f"Script :{script_name} is not present on the server..Enter valid name."}
    return render(request,"result.html",{'res':restf})
            





    