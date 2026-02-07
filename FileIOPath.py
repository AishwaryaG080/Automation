import os

def main():
    Filename = input("Enter the name of file : ")

    Ret = os.path.isabs(Filename)

    if(Ret == True):
        print("It is Absolute Path")
    else:
        print("It is Relative Path")

    

if __name__ == "__main__":
    main()