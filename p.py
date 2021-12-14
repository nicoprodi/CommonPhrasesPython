
def dots(x):
    x = x.replace('?', '.')
    x = x.replace('!', '.')
    x = x.replace('\n', '')
    return x


            # Check if there are the same sentences without spaces
def check(sentence, sentence2):
    for i in sentence:
        for j in sentence2:
            if checkWords(i, j)==1:
                print(i)
                print(j)

            # Check the words
def checkWords(sentence, sentence2):
    while '  ' in sentence:
        sentence = sentence.replace('  ', ' ')
    while '  ' in sentence2:
        sentence2 = sentence2.replace('  ', ' ')
    if sentence == sentence2:
        return 1
    return 0

def main():
    file1=input("File 1 -- ")
    file2=input("File 2 -- ")

    try:
        f = open(file1, "r")
    except IOError:
        print("File 1 not accessible")
        return
    x = f.readline()                        # x contains the strings from first file

    try:
        f2 = open(file2, "r")
    except IOError:
        print("File 2 not accessible")
        return

    y = f2.readline()
    while y:                            # y contains the strings from first file
        y = dots(y)
        sentence2 = y.split(".")
        f = open(file1, "r")
        x = f.readline()
        while x:
            x = dots(x)
            sentence = x.split(".")
            check(sentence, sentence2)
            x = f.readline()
        f.close()
        y = f2.readline()


main()
