
def read():
    numbers = []
    #With permite que ayude a que en caso de error el archivo no se rompa
    with open("./data/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)
def write():
    names = ["Facundo", "Miguel", "Pepe", "Luis", "Nuñez", "Dora" ]
    with open("./data/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()

if __name__ == "__main__":
    run()