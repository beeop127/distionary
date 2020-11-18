import Search


word = input("enter the word : ").lower()
output = Search.searchData(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
