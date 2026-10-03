import shutil
import sys
import os

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg"):
            os.rename(filename, "grp00" + filename[4:])
            #shutil.move("./" + filename, "./maybe")
            print(filename + " and the new name is : \t " + "grp0" + filename[:-6] + ".JPG")

if __name__ == '__main__':
    main()