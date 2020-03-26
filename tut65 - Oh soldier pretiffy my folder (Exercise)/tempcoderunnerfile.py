def removeNewLine(List):
    for string in List:
        newStr = string.replace('\n', '')
        print(string)
        print(newStr)
        List.remove(string)
        List.append(newStr)