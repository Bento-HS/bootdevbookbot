
from stats import wordCounter
from stats import charCounter
from stats import catalogSort
import sys

def tomeRaider(path):
    tomeContents = ""
    with open(path) as tome:
        tomeContents = tome.read()
    wordCounter(tomeContents)    
    return tomeContents

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        tomeString = tomeRaider(path)
        print("==================== BOOKBOT ====================")
        print(f"Analyzing Book found at {path}")
        print("------------------ Word Count -------------------")
        print(f"Found {wordCounter(tomeString)} total words")
        print("---------------- Character Count ----------------")
        #print(charCounter(tomeString))
        allChars = catalogSort(charCounter(tomeString))
        for chara in allChars:
            print(f"{chara["character"]}: {chara["count"]}")
        print("====================== END ======================")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
