
market_2nd = {"ns": "green", "ew": "red"}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "Neither light  is red!" + str(intersection)


switchLights(market_2nd)
