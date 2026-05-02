#change next 2 lines
winas="c:\\MinGW\\bin\\as.exe"
winobj="c:\\MinGW\\bin\\objdump.exe"
import os
def spt(s):
    r=s.split(" ")
    rr=[]
    for a in range(len(r)):
        
        if r[a].strip()!= "":
            rr.append(r[a])
    return rr
print("give me the .o object file name ? ")
a=input().strip()
os.system(winobj+" -x "+a+" > out.txt")

f1=open("out.txt","r")
txt=f1.read()
f1.close()
txts=txt.split("\n")
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>1:
                
                if aa[1].strip()==".text":
                    if len(aa)>5:
                        print("file address: ",end="")   
                        print(aa[5])
                        print("Sections size: ",end="")   
                        print(aa[2])

        if a.strip()=="SYMBOL TABLE:":
             t=False
        if a.strip()=="Sections:":
             t=True