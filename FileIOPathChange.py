import os

def main():
    Filename = input("Enter the name of file : ")

    if(os.path.exists(Filename)):

        Ret = os.path.isabs(Filename)

        if(Ret == True):
            print("It is Absolute Path")
        else:
            print("It is Relative Path")
            Newpath=os.path.abspath(Filename)

            print("Updated path: ",Newpath)

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()