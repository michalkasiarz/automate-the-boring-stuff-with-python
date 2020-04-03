from datetime import datetime
import traceback


# box print

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol needs to be a String of a length 1")
    try:
        if (width < 2) or (height < 2):
            raise Exception("Width and height must be greater or equal to 2")
    except:
        errorFile = open("error_log.txt", "a")
        errorFile.write("\n\n" + str(datetime.fromtimestamp(datetime.timestamp(datetime.now()))) + "\n\n")
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print("The traceback info was written into error_log.txt")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


boxPrint("@", 1, 5)
