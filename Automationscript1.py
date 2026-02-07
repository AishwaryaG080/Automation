import sys

def main():
    border="-"*40
    print(border)
    print("-------- Marvellous Automation ---------")
    print(border)

    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform _______")
            print("This is Automation Scrpit")
        
        elif((sys.argv[1]=="--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScrpitName.py Argument1 Argument2")
            print("Argument1 : ____________")
            print("Argument2 : ____________")
        
        else:
            print("Use the given flags as :")
            print("--u : used to display the usage")
            print("--h : used to display the help")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u : used to display the usage")
        print("--h : used to display the help")
    
    print(border)
    print("-----Thankyou for using our script -----")
    print("-------- Marvellous Infosystems --------")
    print(border)

if __name__ == "__main__":
    main()