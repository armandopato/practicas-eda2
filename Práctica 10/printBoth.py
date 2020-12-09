from typing import TextIO


def printBothFactory(openedFile: TextIO):
    def printBoth(*toPrint):
        formattedStr = " ".join([str(element) for element in toPrint])
        print(formattedStr)
        openedFile.write(formattedStr + "\n")
    return printBoth
