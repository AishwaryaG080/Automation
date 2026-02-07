import os

def main():
    Filename = input("Enter the name of file : ")

    if(os.path.exists(Filename)):

        os.remove(Filename)
        print("File gets deleted")

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()