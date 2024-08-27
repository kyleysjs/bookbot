def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()


    lettercount = {}
    count = 0
    for i in words:
        count += 1
        myword = i.lower()
        for letter in myword:
            if letter not in lettercount:
                lettercount[letter] = 1
                continue
            lettercount[letter] += 1

    listofvalidchars =[]


    letcount = lettercount
    sorteddict = {}
    for i in range(0, len(lettercount), 1):
        max = float("-inf")
        keymax = {"init": 0}
        for let in letcount:
            if letcount[let] > max:
                max = letcount[let]
                currkey = list(keymax.keys())[0]
                del keymax[currkey]
                keymax[let] = letcount[let]
        for key in keymax:
            if key.isalpha():
                sorteddict[key] = keymax[key]
        del letcount[key]

    print(f"---Begin report---\n{count} words in document")
    for each in sorteddict:
        print(f"The character {each} was found {sorteddict[each]} times.")
    print("--- End report ---")


main()
