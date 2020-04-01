
# box print

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol needs to be a String of a length 1")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


boxPrint("@s", 15, 5)
