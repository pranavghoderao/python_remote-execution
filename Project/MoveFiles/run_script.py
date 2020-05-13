from MoveFiles.models import Documents
import subprocess
from subprocess import Popen,PIPE,STDOUT

class execution():

    def runScriptPython(self,id,par,p):
        
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
        
        cmd =" cd /home/vagrant/scripts; chmod +x {}; ./{}".format(p)

        try:
            stdin,stdout,stderr=par.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            result = {"status":"Success","output":str(op)}
        
        except Exception as e:
            result = {"status":"Failed","output":str(e)}

        return result