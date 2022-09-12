#technical tests 4

def reverse(text):
    if text == "":
        return text
    else:
        turn_over = text[0]
        text = text[1:]
        return reverse(text) + turn_over


if __name__ == '__main__':
    text = "HelloWorld!"
    result= reverse(text)
    print(result)
