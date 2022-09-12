#technical test 3

def getFirstUpperChar(text):
    try:
        upper_char = "NA"
        index_search = 0
        char = text[index_search]
        found = char.isupper()
        if found:
            upper_char = char
            return upper_char
        else:
            text = text[1:] 
            return getFirstUpperChar(text)
    except IndexError as IE:
        return upper_char


if __name__ == '__main__':
    text = "helloWorld"
    getFirstUpperChar(text)