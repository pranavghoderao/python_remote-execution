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





    