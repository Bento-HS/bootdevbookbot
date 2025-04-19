def wordCounter(tomeString):
    return len(tomeString.split())

def charCounter(tomeString):
    charCatalog = {}
    tomeArray = list(tomeString.lower())
    #print(f"{len(tomeArray)} to start")
    while len(tomeArray) > 0:
        if tomeArray[-1] in charCatalog:
            pass
        else:
            #print(f"Logging {tomeArray[-1]}")
            charCatalog[tomeArray[-1]] = tomeArray.count(tomeArray[-1])
        #print(f"Deleting {tomeArray[-1]}")
        tomeArray.pop()
        #print(f"{len(tomeArray)} characters remain")
    return charCatalog

def orderBy(dict):
    return dict["count"]

def catalogSort(charCatalog):
    catalogList = []
    for char,count in charCatalog.items():
        if char.isalpha():
            temp = {}
            temp["character"] = char
            temp["count"] = count
            catalogList.append(temp)
    catalogList.sort(reverse=True,key=orderBy)
    return(catalogList)
