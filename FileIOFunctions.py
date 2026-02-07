import os

def main():
    Filename = input("Enter the name of file : ") #Demo.txt

    if(os.path.exists(Filename)):

        fobj=open(Filename,"r")

        print(fobj.name) #Demo.txt
        print(fobj.mode) #r
        print(fobj.closed) #False

        fobj.close()
        print(fobj.closed) #True

    
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()