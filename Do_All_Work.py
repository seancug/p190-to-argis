import ArgisTXT
import os

files = os.listdir('.')
wfp = open('all.txt', 'w')
for sg in files:
    if ".p190" in sg:
        wdata = ArgisTXT.Transform(sg)
        wfp.writelines(wdata)

wfp.close()