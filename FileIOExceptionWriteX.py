def main():
    try:
        fobj= open("Hello.txt","w")    
        print("File gets sucessfully opened")

        fobj.write("Jay Ganesh Marvellous...")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()