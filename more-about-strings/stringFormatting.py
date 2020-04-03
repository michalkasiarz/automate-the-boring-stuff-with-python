# String formatting

name = "Alice"
place = "Main Street"
time = "6 pm"
food = "turnips"

print("Hello " + name +
      ", you are invited to a party at " +
      place +
      " at " +
      time +
      ". Please bring " +
      food + ".")

print("Hello %s, you are invited to a party at %s at %s. Please bring %s." % (name, place, time, food))
