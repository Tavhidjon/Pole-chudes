import random
mevaho = {
    "Apple": "меваи ширин ",
    "Banana": "меваи мулоим ва ширин, ки бо калий бой аст",
    "Orange": "меваи ситрусӣ ва шарбатдор",
    "Mango": "меваи тропикӣ бо маззаи ширин ва турш",
    "Grapes": "меваҳои хурд ва шарбатдор, ки аксар вақт барои истеҳсоли шароб истифода мешаванд"
}
a = random.choice(list(mevaho.keys())).lower()
def con(meva, guesses):
    return ''.join([i if i in guesses else '*' for i in meva])
print(f"Podsakzka: In meva {mevaho[a.capitalize()]}.")
g = set()
while True:
    yoftagi = input("Як ҳарфро тахмин кунед (ё 'exit'-ро нависед, то бароед):").lower()
    if yoftagi == 'exit':
        print("Ташаккур барои бозӣ кардан!")
        break
    g.add(yoftagi)
    s = con(a, g)
    print(s)
    if '*' not in s:
        print("Табрик! Шумо калимаро дуруст тахмин кардед!")
        break
