from random import randint

def addsoz():
    while True:
        soz = input("uz>>>")
        word = input("en>>>")
        if soz == 'sstop' or word == 'sstop':
            break
        with open('filesoz.txt', 'a') as fayl:
            fayl.write(soz + '\n')

        with open('fileword.txt', 'a') as fayl:
            fayl.write(word + '\n')
        if soz == 'sstop' or word == 'sstop':
            break


def start_test():
    with open('filesoz.txt') as file:
        sozlar = file.readlines()
    with open('fileword.txt') as file:
        words = file.readlines()

    sozlar = [soz.rstrip() for soz in sozlar]
    words = [word.rstrip() for word in words]


    tanlov=input(">>>[enuz/uzen]\n>>>")

    if tanlov=='enuz':
        while True:
            a = randint(1, len(sozlar)-1)
            print(f">>>{sozlar[a]}")
            tarjima=input(">>>")
            if tarjima=='sstop':
                break
            if tarjima==words[a]:
                print(">>> ✅\n")
            else:
                print(f">>> ❌\n{words[a]}\n")
    elif tanlov=="uzen":
        while True:
            a = randint(1, len(sozlar)-1)

            print(f">>>{words[a]}")
            tarjima=input(">>>")
            if tarjima=='sstop':
                break
            if tarjima==sozlar[a]:
                print(">>> ✅\n")
            else:
                print(f">>> ❌\n{sozlar[a]}\n")


aa=input(">>>[addsoz/test]\n>>>")
if aa=='addsoz':
    addsoz()
elif aa=='test':
    start_test()
else:
    exit()
