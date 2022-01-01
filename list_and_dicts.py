
def main():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {'fistname': "Luis", "lastmame": "Nunez"}
    
    super_list = [
        {'fistname': "Luis", "lastmame": "Nunez"},
        {'fistname': "Fernando", "lastmame": "Rangel"},
        {'fistname': "Pepe", "lastmame": "Garcia"},
        {'fistname': "Susana", "lastmame": "Perez"},
    ]
    
    super_dict = {
        "Natural_nums": [1,2,3,4,5],
        "Integer_nums": [-1,0,1,2,4],
        "Floating_nums": [1.2, 4.5, 7.45]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    main()