people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # 1. Creamos una nueva lista vacía
    new_list = []
    
    # 2. Iteramos sobre la lista original
    for person in people:
        # 3. Si la persona actual NO es la que queremos borrar, la agregamos
        if person != person_name:
            new_list.append(person)
            
    # 4. Devolvemos la lista filtrada
    return new_list

# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))