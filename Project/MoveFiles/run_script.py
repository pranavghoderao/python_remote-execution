from MoveFiles.models import Documents
from subprocess import Popen,PIPE,STDOUT
import subprocess
import os


class execution():

    def runScriptPython(self,id,par,p):
        print("inside python..")
        cmd = " cd /home/vagrant/scripts; python {}".format(p)
        
        try:
            stdin,stdout,stderr=par.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            result = {"status":"Success","output":str(op)}
        
        except Exception as e:
            result = {"status":"Failed","output":str(e)}

        return result

    def runScriptShell(self,id,par,p):
        print("inside shell..")
        print (p)
        #cmd =" cd /home/vagrant/scripts; chmod +x {}; ./{}".format(p,p)
        cmd = f" cd /home/vagrant/scripts ; chmod +x {p} ; ./{p}"
        print(cmd)
        try:
            stdin,stdout,stderr=par.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            result = {"status":"Success","output":str(op)}
        
        except Exception as e:
            result = {"status":"Failed","output":str(e)}

        return result

    def remoteRunShell(self,loc,scriptname,par):
        print("inside remoteRunPython..")

        cmd= f" cd {loc}; chmod +x {scriptname}; ./{scriptname}"
        print(cmd)
        try:
            stdin,stdout,stderr=par.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            result = {"status":"Success","output":str(op)}
        
        except Exception as e:
            result = {"status":"Failed","output":str(e)}

        return result

    def remoteRunPython(self,loc,scriptname,par):
        print("inside remoteRunShell..")

        cmd= f" cd {loc}; python {scriptname} "
        print(cmd)
        try:
            stdin,stdout,stderr=par.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            result = {"status":"Success","output":str(op)}
        
        except Exception as e:
            result = {"status":"Failed","output":str(e)}

        return result


    def getFileNames(self,par):
        print("Inside getFilesNames..")
        filenames =[]
        i = 0
        cmd = "find /home/vagrant/scripts -name '*.py'; find /home/vagrant/scripts -name '*.sh' "
        #cmd =" cd /home/vagrant/scripts; ls"
        stdin,stdout,stderr=par.exec_command(cmd)
        op=stdout
        op=" ".join(op)
        print(op)

        names=op.splitlines()
        print(names)
        
        for o in names:
            path=os.path.basename(o)
            print(path)
            filenames=filenames + [path]

        print(filenames)   
        return filenames
        
            

       


