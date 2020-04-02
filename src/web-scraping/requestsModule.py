import requests

# Requests module

responseObject = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(responseObject.status_code)

# length of the response
print(len(responseObject.text))

# printing the first 500 characters using slicing

print(responseObject.text[:500])

# bad request and raise example

# badRequest = requests.get("https://automatetheboringstuff.com/files/asdaaxwww3")
# badRequest.raise_for_status()

print("-----------------")

# write-binary mode
playFile = open("RomeoAndJuliet.txt", "wb")

for chunk in responseObject.iter_content(100000):
    playFile.write(chunk)
    print(chunk)

playFile.close()
