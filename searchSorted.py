import main
getUserName = main.getUserName()

getUserData = main.transferUserData()

getSortedData = main.transferSortedData()

getSearchIndex = main.transferIndex()
print(getSearchIndex)

search_key = input('enter search key')
if search_key in getUserData:
    print('here is your search... ', search_key)
else:
    print('not found')


















