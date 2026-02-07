def main():
    try:
        open("Hello.txt","w")    
        print("File gets sucessfully opened")
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    finally:
        print("End of Application")
if __name__ == "__main__":
    main()