import maya.cmds as mc
import subprocess
import os

def fileCollect():
    curProj = mc.workspace(q=True,fullName=True)
    siPath = curProj + r"/sourceimages"
    siPath = siPath.replace("/","\\")

    a = mc.ls(type="file")
    l = len(a)
    for i in range(l):
        b = mc.getAttr("{}.fileTextureName".format(a[i]))
        b2 = b.replace("/","\\")
        cmd = r'copy {} {}'.format(b2,siPath)
        returncode = subprocess.Popen(cmd, shell=True)
        bn = os.path.basename(b)
        bn = "sourceimages\\" + bn
        print bn
        mc.setAttr("{}.fileTextureName".format(a[i]), bn, type="string" )

        # c = mc.setAttr("{}.fileTextureName".format(a[i]), path, type="string" )

    # for i in range(l):
    #     c = mc.setAttr("{}.fileTextureName".format(a[i]), path, type="string" )
# setAttr -type "string" file1.fileTextureName "D:/TESTTEST/outProjecttex/test2.tif";
def mainWin():
    cmds.window(title='fileCollect', w=200)
    cmds.columnLayout(adj=True)
    cmds.separator( h=3 )
    cmds.text("fileCollect_V1")
    cmds.separator( h=3 )
    cmds.button( label = 'Do it!', w=100, h=40, command='fileCollect()')

    cmds.showWindow()

mainWin()
