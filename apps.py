import copy
x=0
heads_="""
import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk,title:str,text:str,backgrouds:str,foregrounds:str):
        self.root=root
        self.root.title(title)
        self.root.geometry("640x480")
        self.root.configure(background=backgrouds)

"""


legs="""
        self.$2$1=tk.$2(background=backgrouds,foreground=foregrounds)
        self.$2$1.pack(padx=10,pady=10)
"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()


def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value):
    global x
    print("handle : function :"+value)
    x=x+1
    zzz=copy.copy(legs)
    zzz=zzz.replace("$1",str(x))
    zzz=zzz.replace("$2",value)
    saves(files,"a",zzz)
    

print(filesa)
gfiles=getfiles(filesa)

filesa=filesa.replace(".txt",".py")
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)








heads___="""
backgrouds="black"
foregrounds="white"
text=""
title="project"
root=tk.Tk()
apps=myapps(root,title,text,backgrouds,foregrounds)
root.mainloop()

"""
saves(filesa,"a",heads___)