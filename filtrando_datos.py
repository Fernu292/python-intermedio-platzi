DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    #filtrando datos de los programadores de python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # print(all_python_devs)
    
    #filtrando trabajadores de platzi
    all_Platzzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # print(all_Platzzi_workers)
    
    #Todos los trabajadores adultos 
    adults = list( filter(lambda worker: worker["age"] >=18, DATA) )
    adults = list(map(lambda worker: worker["name"], adults))
    # print(adults)

    #Personas mayores a 70
    old_people = list(map(lambda worker: worker | {"old" : worker["age"]>70}, DATA))
    
    # print(old_people)
    
    #Reto, utilizar higth order funcions con las listas hechas con list 
    #comprehensions y a la inversa 
    
    #Python devs
    all_python_devs = list( filter(lambda worker: worker["language"] == "python", DATA) )
    all_python_devs = list( map(lambda worker: worker["name"], all_python_devs) )
    # print(all_python_devs)
    
    #Trabajadores de platzi
    all_Platzzi_workers = list( filter(lambda worker: worker["organization"]=="Platzi", DATA) )
    all_Platzzi_workers = list( map(lambda worker : worker["name"], all_Platzzi_workers) )
    
    # print(all_Platzzi_workers)
    
    #adults
    adults = [worker["name"] for worker in DATA if worker["age"] >=18]
    # print(adults)
    
    #personas mayores de la tercera edad
    #para agregar llaves a un diccionario en list comprehensions usamos 
    # {**diccionario, **{'llave nueva': valor}}
    old_people = [{**worker, **{"old": worker["age"]>70}} for worker in DATA ]
    # print(old_people)
if __name__ == '__main__':
    main()