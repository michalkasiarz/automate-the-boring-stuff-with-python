# More dict methods

# get method

myCat = {"size": "fat", "color": "gray", "disposition": "lazy"}

print(myCat.get("origin", "Unknown"))   # returns Unknown if there is no "origin" key

# setDefault method
myCat.setdefault("origin", "it's own country")

print(myCat["origin"])      # default value, because it hasn't been set otherwise
