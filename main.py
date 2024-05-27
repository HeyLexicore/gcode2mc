import math
import os

import amulet

path = "C:\\absoulute\\path\\to\\your\\minecraft\\world\\folder"
model = "model.gcode"
scale=2

def dist(t1,t2):
    d = math.sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2+(t1[2]-t2[2])**2)
    return d

def lerp(p0,p1,t):
    x0, y0, z0 = p0
    x1, y1, z1 = p1

    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    z = z0 + (z1 - z0) * t

    return (int(x), int(y), int(z))
def rem(x):
    n=""
    for m in x:
        if m==";":
            break
        n+=m
    return n

def parse_inst(inst):
    x,y,z=(None,None,None)
    inst = rem(inst)
    split = inst.split()
    for n in split:

        #print(n)
        if n[0] == "X":
            x = float(n[1:])*scale
        if n[0]=="Y":
            z=float(n[1:])*scale
        if n[0]=="Z":
            y=float(n[1:])*scale


    return(x,y,z,"E" in "".join(n))

os.system("rm -r '"+path+"\\region'")

level = amulet.load_level(path)
block = amulet.Block("minecraft","stone")
#print(level.bounds("minecraft:overworld"))

#print(f)
fl = open(model, "r")
f=fl.readlines()
fl.close()
f = [i for i in f if "G1" in i]


def run():
    global f

    print(f)
    c=-1
    x, y, z = (0, 0, 0)
    nx,ny,nz = (0,0,0)
    for m in f:
        c+=1
        print(c,len(f)-c,len(f))
        x1,y1,z1,p = parse_inst(m)

        if x1 != None:
            nx=int(x1)
        if y1 != None:
            ny=int(y1)
        if z1 != None:
            nz=int(z1)
        if p and lp:

            print(m)
            d = dist((x,y,z),(nx,ny,nz))

            for i in range(int(d)):
                mx,my,mz = lerp((x,y,z),(nx,ny,nz),i/d)

                level.set_version_block(mx,my,mz,"minecraft:overworld",("java",(1,19,2)),block)
            x,y,z=(nx,ny,nz)
        lp = p
        if "E" not in m:
            lp = False

try:
    run()

finally:
    level.save()
    level.close()
