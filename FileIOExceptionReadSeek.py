def main():
    try:
        fobj= open("Hello.txt","r") 

        print("File gets sucessfully opened")

        print("Current offset is : ", fobj.tell()) #0

        fobj.seek(7)

        print("Current offset is : ", fobj.tell()) #7

        Data=fobj.read(10)

        print("Current offset is : ", fobj.tell()) #17

        print("Data from file is : ", Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main() 