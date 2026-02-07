import sys 
import os

def DirectoryScanner(DirName="Marvellous"):
    
    Ret=False
    
    Ret=os.path.exists(DirName)
    
    if(Ret==False):
        print("There is no such Directory")
        return
    
    Ret=os.path.isdir(DirName)

    if(Ret==False):
        print("It is not a Directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
       for fname  in FileName:
           print("File Name :",fname)



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
            
if __name__ == "__main__":
    main()