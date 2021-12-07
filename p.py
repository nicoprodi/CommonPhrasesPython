
def main():

    f = open("demofile.txt", "r")
    x = f.read()
    f2 = open("demofile2.txt", "r")
    y=f2.read()

    x = x.replace('?', '. ')
    y = y.replace('?', '. ')
    x = x.replace('!', '. ')
    y = y.replace('!', '. ')
    sc = x.split(".")
    x = x.replace('\n', ' ')
    y = y.replace('\n', ' ')
    x = x.replace('  ', '')
    y = y.replace('  ', '')

    sentence1 = x.split(".")
    sentence2 = y.split(".")
    sentence1[len(sentence1)-1] = '1'
    sentence2[len(sentence2)-1] = '2'
    count = 0
    for i in sentence1:
        for j in sentence2:
            if i==j:
                print(sc[count])
        count=count+1

main()