import os

def main():
    Filename = input("Enter the name of file : ")

    Ret = os.path.exists(Filename)

    if (Ret==True):
        fobj=open(Filename,"r")
        print("File gets sucessfully opened")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()