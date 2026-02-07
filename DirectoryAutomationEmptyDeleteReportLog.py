import sys 
import os

def DirectoryScanner(DirName="Marvellous"):
    border = "-"*50

    fobj=open("Marvellous.log","w")

    fobj.write(border+"\n")
    fobj.write("This is a Log File created by Marvellous Automation\n")
    fobj.write("This is a Directory cleaner script\n")
    fobj.write(border+"\n")
    
    Ret=False
    
    Ret=os.path.exists(DirName)
    
    if(Ret==False):
        print("There is no such Directory")
        return
    
    Ret=os.path.isdir(DirName)

    if(Ret==False):
        print("It is not a Directory")
        return
    
    fileCount=0
    EmptyFileCount=0

    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
      
       for fname in FileName:
           fileCount=fileCount+1
           fname=os.path.join(FolderName,fname)

           if(os.path.getsize(fname)==0): #Empty File
               EmptyFileCount=EmptyFileCount+1
               os.remove(fname)

    
    fobj.write("Total Files Scanned: "+str(fileCount)+"\n")
    fobj.write("Total Empty Files Found"+str(EmptyFileCount)+"\n")
    fobj.write(border+"\n") 
    fobj.close()
               


def main():
    border = "-"*50
    print(border)
    print("---------------Marvellous Directory Automation----------------") 
    print(border) 

    if(len(sys.argv)!=2):
        print("Invalid no. of Arguments") 
        print("Please specify the name of Directory")
        return
    
    DirectoryScanner(sys.argv[1])

    print(border)
    print("---------------Marvellous Directory Automation----------------") 
    print(border) 

    
    

if __name__ == "__main__":
    main()