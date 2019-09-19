def main():

    start_word = str.lower(input("Enter a word: "))
    wordA = start_word.replace ("a", "A")
    wordE = wordA.replace ("e", "E")
    wordI = wordE.replace ("i", "I")
    wordO = wordI.replace ("o", "O")
    wordU = wordO.replace ("u", "U")

    print (wordU)

main()

