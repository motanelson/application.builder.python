import copy
x=0
heads_="""
import tkinter as tk
from tkinter import messagebox



class myapps:
    def __init__(self,root:tk.Tk,title:str,text:str,backgrouds:str,foregrounds:str):
        self.root=root
        self.root.title(title)
        self.root.geometry("640x480")
        self.root.configure(background=backgrouds)

"""


legs="""
        self.$1=tk.$2(background=backgrouds,foreground=foregrounds$3)
        self.$1.pack(padx=10,pady=10)
"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()
filesaa=copy.copy(filesa)

def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value:str):
    global x
    print("handle : function :"+value)
    x=x+1
    v=value.split("|")
    v1=""
    v2=""
    v3=""
    v4=""
    if len(v)==2:
       v1=v[0].strip()
       v2=v[1].strip()
    if len(v)==1:
       v1=v[0].strip()+str(x)
       v2=v[0].strip()
    if len(v)==3:
       v1=v[0].strip()
       v2=v[1].strip() 
       v3=v[2].strip() 
    if len(v)>3:
       v1=v[0].strip()
       v2=v[1].strip() 
       v3=v[2].strip()
       v4=v[3].strip()
    zzz=copy.copy(legs)
    zzz=zzz.replace("$1",v1)
    zzz=zzz.replace("$2",v2)
    zzz=zzz.replace("$3",v3)
    zzz=zzz.replace("$4",v4)
    zzz=zzz.replace("\\n","\n")
    zzz=zzz.replace("~","\\n")
    saves(files,"a",zzz)
    

print(filesa)
gfiles=getfiles(filesa)

filesa=filesa.replace(".txt",".py")
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)

legs2="""
    def $1_handler(self):
        #put you code here
        $4

"""
def defs1(files,value:str):
    global x
    print("handle : function :"+value)
    x=x+1
    v=value.split("|")
    v1=""
    v2=""
    v3=""
    v4="pass"
    if len(v)==2:
       v1=v[0].strip()
       v2=v[1].strip()
    if len(v)==1:
       v1=v[0].strip()+str(x)
       v2=v[0].strip()
    if len(v)==3:
       v1=v[0].strip()
       v2=v[1].strip() 
       v3=v[2].strip() 
    if len(v)>3:
       v1=v[0].strip()
       v2=v[1].strip() 
       v3=v[2].strip()
       v4=v[3].strip()
    zzz=copy.copy(legs2)
    zzz=zzz.replace("$1",v1)
    zzz=zzz.replace("$2",v2)
    zzz=zzz.replace("$3",v3)
    zzz=zzz.replace("$4",v4)
    zzz=zzz.replace("\\n","\n")
    zzz=zzz.replace("~","\\n")
    saves(files,"a",zzz)


gfiles=getfiles(filesaa)

print("debug")

for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs1(filesa,sss)




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