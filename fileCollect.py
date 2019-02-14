import maya.cmds as mc
import subprocess

def fileCollect():
    curProj = mc.workspace(q=True,fullName=True)
    siPath = curProj + r"/sourceimages"
    siPath = siPath.replace("/","\\")

    a = mc.ls(type="file")
    l = len(a)
    for i in range(l):
        b = mc.getAttr("{}.fileTextureName".format(a[i]))
        b = b.replace("/","\\")
        cmd = r'copy {} {}'.format(b,siPath)
        returncode = subprocess.Popen(cmd, shell=True)

fileCollect()
