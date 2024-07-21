import pandas as pd

print("NOOB Finder 4000")
print("----------------")

myId = int(input("Input your Roblox User ID: "))
friendApiUrl = f'https://friends.roblox.com/v1/users/{myId}/friends'
myFriends = {}
jsonData = pd.read_json(friendApiUrl)
for friend in jsonData.data:
    myFriends[friend["id"]] = [friend["name"], friend["displayName"]]
print("Friend list loaded")

print("----------------")
print("Reading The N.O.O.B. spreadsheet...")
noobSheet = '1QwVTwGgAqK6XZSM_smobXvHOXnOtCYvKYdku0r4SbqY'
url = f'https://docs.google.com/spreadsheets/d/{noobSheet}'
sheetDF = pd.read_html(
    url, attrs={'class': 'waffle'}, skiprows=1
)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')
print("Complete")
print("----------------")
print("Searching...")

matches = 0
for userId in sheetDF.get("User ID"):
    val = myFriends.get(userId, None)
    if val is not None:
        print(f"Found: {val[0]} ({val[1]}) - https://roblox.com/users/{userId}/profile")
        matches += 1

if matches == 1:
    print("1 match")
else:
    print(f"{matches} matches")
