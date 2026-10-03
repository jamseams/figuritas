import shutil
import sys
import os

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    for filename in os.listdir(directory):
        if filename.lower().endswith("_1.jpeg") or filename.lower().endswith("_1.jpg"):
            #os.rename(filename, "grp4" + filename)
            shutil.move("./" + filename, "./maybe")
            print(filename + " and the new name is : \t " + "grp4" + filename )

if __name__ == '__main__':
    main()