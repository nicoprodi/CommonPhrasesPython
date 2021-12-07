
def main():
    #file1=input("File 1 -- ")
    #file2=input("File 2 -- ")

    try:
        f = open("demofile.txt", "r")
    except IOError:
        print("File 1 not accessible")
        return
    x = f.read()                        # x contains the strings from first file

    try:
        f2 = open("demofile2.txt", "r")
    except IOError:
        print("File 2 not accessible")
        return
    y = f2.read()                         # y contains the strings from first file

    x = dots(x)
    y = dots(y)

    sentence = x.split(".")
    sentence2 = y.split(".")

    check(sentence, sentence2)


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

main()
