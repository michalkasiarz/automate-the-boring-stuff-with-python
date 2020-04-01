import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# turning on/off logging module message
logging.disable(logging.CRITICAL)

# Log levels:
# logging.DEBUG (the lowest)
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL (the highest)


logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.debug("Return value is %s" % total)
    return total


print(factorial(5))

logging.debug("End of program")
