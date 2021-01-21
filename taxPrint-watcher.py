import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil
import glob

srcDir = "C:/GDT-test/CLIENTS/zClient Print Files/"

class Handler(FileSystemEventHandler):
  def on_modified(self, event):
    for f in os.listdir(srcDir):
      try:
        destPath = fileParser(f)
        if not os.path.exists(destPath):
          os.makedirs(destPath) 
        if os.path.exists(destPath):
          if os.path.isfile(destPath +"/" + f):
            print("dupicate file: " + f)
            shutil.move(srcDir+f,destPath+"/"+f+"-DUPLICATE.txt")
            print("moved: " + f)
          else: shutil.move(srcDir+f,destPath)
          print("moved: " + f)
      except:
        print("error moving file")
  
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

def main():
  observer = Observer()
  event_handler = Handler()
  observer.schedule(event_handler,srcDir,recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(10)
  except KeyboardInterrupt:
    observer.stop()

  observer.join()


main()


