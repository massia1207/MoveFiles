import os
import shutil
import glob
from win10toast import ToastNotifier

notifier = ToastNotifier()

def main():
  srcDir = "C:/GDT-test/CLIENTS/zClient Print Files/"
  moveFile(srcDir)

def fileParser(file):
  year = file[:4] 
  clientID = file[8:12]
  alpha = ""
  clientPath = ""
  if (clientID[0]) in ("ABCD"):
    alpha = "ABCD"
  elif clientID[0] in ("EFGH"):
    alpha = "EFGH"
  elif clientID[0] in ("IJKL"):
    alpha = "IJKL"
  elif clientID[0] in ("MNOP"):
    alpha = "MNOP"
  elif clientID[0] in ("QRST"):
    alpha = "QRST"
  elif clientID[0] in ("UVWX"):
    alpha = "UVWX"
  elif clientID[0] in ("YZ"):
    alpha = "YZ"
  else: print('error parsing filename')
    
  for dir in glob.glob("c:/GDT-Test/CLIENTS/" + alpha + "/" + clientID + "*"):
    clientPath = dir

  return clientPath + "/Tax/" + year

def moveFile(srcDir):
  for f in os.listdir(srcDir):
    try:
      destPath = fileParser(f)
      if not os.path.exists(destPath):
        os.makedirs(destPath) 
      if os.path.exists(destPath):
        if os.path.isfile(destPath +"/" + f):
          print("dupicate file: " + f)
          notifier.show_toast("GDT File Mover","duplicate file error: " + f)
          print(destPath+f+"-DUPLICATE.txt")
          shutil.move(srcDir+f,destPath+"/"+f+"-DUPLICATE.txt")
        else: shutil.move(srcDir+f,destPath)
    except:
      print("error moving file")

main()


