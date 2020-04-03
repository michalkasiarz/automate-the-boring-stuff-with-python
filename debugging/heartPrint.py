# heart print

def heartPrint(symbol):
    a = 3
    print(" " * a + (symbol * (a * 2)) + (" " * a) + (symbol * (a * 2)))
    print((symbol * a) + (" " * (a * 2)) + (symbol * a) + (" " * (a * 2)) + (symbol * a))
    print((symbol * a) + (" " * (a * 2)) + (symbol * a) + (" " * (a * 2)) + (symbol * a))
    print((" " * (a - 2)) + (symbol * 2) + (" " * (a * 2 + 1)) + symbol + (" " * a * 2) + (symbol * 2))
    print((" " * (a)) + (symbol * 2) + (" " * ((a * 4) - 1)) + (symbol * 2))
    print((" " * (a + 2)) + (symbol * 2) + (" " * ((a * 3) - 2)) + (symbol * 2))
    print((" " * (a + 4)) + (symbol * 2) + (" " * a) + (symbol * 2))
    print((" " * (a + 6)) + (symbol * 3))
    print((" " * (a + 7)) + symbol)

heartPrint("\u2665")
