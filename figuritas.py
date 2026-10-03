import sys
import re

def main():
    lName = sys.argv[1] if len(sys.argv) > 1 else 'dobles.txt'
    rName = sys.argv[2] if len(sys.argv) > 2 else 'faltan.txt'

    rFile = open(rName, 'r')
    lFile = open(lName, 'r')

    lData = [int(x.strip(' ')) for x in filter(None, re.split(';|,', lFile.read().replace('\n', ',').replace('\t', ',')))]
    rData = [int(y.strip(' ')) for y in filter(None, re.split(';|,', rFile.read().replace('\n', ',').replace('\t', ',')))]

    sortedList = sorted(list(set(lData).intersection(rData)))

    print(lName + " contains : " + str(len(list(lData))) + " entries and " + rName + " contains : " + str(len(list(rData))) + " entries.")

    print("A total of " + str(len(sortedList)) + " Stickers. ")
    print(', '.join(map(str, sortedList)))


if __name__ == '__main__':
    main()