import os

def main():
    Filename = input("Enter the name of file : ") #Demo.txt

    if(os.path.exists(Filename)):

        fobj=open(Filename,"w")
        print(fobj.readable())
        print(fobj.writable())
        print(fobj.seekable())

    
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()