import random

mevaho = {
    "Apple": "меваи ширин",
    "Banana": "меваи мулоим ва ширин, ки бо калий бой аст",
    "Orange": "меваи ситрусӣ ва шарбатдор",
    "Mango": "меваи тропикӣ бо маззаи ширин ва турш",
    "Grapes": "меваҳои хурд ва шарбатдор, ки аксар вақт барои истеҳсоли шароб истифода мешаванд"
}

k = []

def play_game():
    a = random.choice(list(mevaho.keys())).lower()

    def con(meva, guesses):
        return ''.join([i if i in guesses else '*' for i in meva])

    print(f"Podsakzka: In meva {mevaho[a.capitalize()]}.")
    print(f"Kalima: {'*' * len(a)}") 

    g = set()

    while True:
        yoftagi = input("Як ҳарфро тахмин кунед (ё 'exit'-ро нависед, то бароед):").lower()
        if yoftagi == 'exit':
            print("Ташаккур барои бозӣ кардан!")
            break
        if yoftagi == a:
            print(f"Табрик! Шумо калимаро дуруст тахмин кардед! Калима: {a.capitalize()}")
            k.append(a.capitalize())
            break
        if len(yoftagi) == 1 and yoftagi in a:
            g.add(yoftagi)
            s = con(a, g)
            print(s)
            if '*' not in s:
                print(f"Табрик! Шумо калимаро дуруст тахмин кардед! Калима: {a.capitalize()}")
                k.append(a.capitalize())
                break
        else:
            print(f"Шумо бохтед! Калимаи дуруст: {a.capitalize()}")
            break

    z = input("Шумо мехоҳед бозӣ кунед? (yes/no): ").lower()
    if z == 'yes':
        play_game()
    else:
        print("Ташаккур барои бозӣ кардан!")
        print("Шумо ин калимаҳоро тахмин кардед:")
        for i, word in enumerate(k, 1):
            print(f"{i}. {word}")

play_game()
