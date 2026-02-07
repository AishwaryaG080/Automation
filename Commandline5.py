# Commandline4.py 11 10
# PYPI.ORG
import sys

def main():
    if (len(sys.argv)< 3 or len(sys.argv)>3):
        print("Invalid no of arguments")
    else:
        no1=int(sys.argv[1])
        no2=int(sys.argv[2])
        print (no1+no2)

if __name__ == "__main__":
    main()