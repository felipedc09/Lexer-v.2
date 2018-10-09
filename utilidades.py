
def readLinesFile(fileName):
    elements = []
    try:
        with open(fileName) as File:
            elements = File.readlines()
    finally:
        File.close()
    return elements


def writeInFile(fileName, content):
    try:
        File = open(fileName, "w")
        File.write(content)
    finally:
        File.close()


def appendInFile(fileName, content):
    try:
        File = open(fileName, "a")
        File.write("\n" + content)
    finally:
        File.close()