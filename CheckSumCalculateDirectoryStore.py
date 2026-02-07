import hashlib
import os



def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName="Marvellous"):
    Ret=False
    Ret=os.path.exists(DirectoryName)

    if(Ret==False):
        print("There is no such Directory")
        return
    
    Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("There is no such Directory")
        return
    
    Duplicate={}

    for FolderName,SubfolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            checkSum=CalculateCheckSum(fname)

            if checkSum in Duplicate:
                Duplicate[checkSum].append(fname)
            else:
                Duplicate[checkSum] = [fname]

    return Duplicate

def DisplayResult(MyDict):
    Result=list(filter(lambda x : len(x) > 1, MyDict.values()))  

    count=0

    for value in Result:
        for subvalue in value:
            count=count+1
            print(subvalue)
        
        print("Value of count is :",count)
        count=0

def DeleteDuplicate(Path = "Marvellous"):
    Mydict = FindDuplicate(Path)

    Result=list(filter(lambda x : len(x) > 1, Mydict.values()))  

    count=0
    cnt=0

    for value in Result:
        for subvalue in value:
            count=count+1
            if(count>1):
                print("Deleted file : ", subvalue)
                os.remove(subvalue)
                cnt=cnt+1
        count=0
    print("Total Deleted Files : ",cnt)

def main():
    
    DeleteDuplicate()

if __name__ == "__main__":
    main()