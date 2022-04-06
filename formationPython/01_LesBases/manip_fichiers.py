import os
folder_path = os.path.join(os.path.curdir, "exports")
base_file_path = os.path.join(folder_path, "test")

# Manipulation des fichiers textes
file_path = base_file_path + ".txt"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

print("=== LECTURE ===")
if os.path.exists(file_path):
    # f = open(file_path, 'r')
    # print(f.read())
    # f.close()

    with open(file_path, 'r') as f:  # Eviter d'avoir à fermer le fichier manuellement
        content = f.read()
        f.seek(0)
        content_repl = repr(f.read())
        f.seek(0)
        content_readlines = f.readlines()
        f.seek(0)
        content_better = f.read().splitlines()
        print(content)
        print(content_repl)
        print(content_readlines)
        print(content_better)

print("=== ECRITURE ===")
with open(file_path, 'w') as f:  # Ecriture
    f.write(input("Ecrivez une dans le fichier : "))

print("=== APPEND ===")
with open(file_path, 'a') as f:
    f.write('\n' + input("Ajoutez une ligne dans le fichier : "))


if os.path.exists(folder_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Manipulation des JSON
import json
file_path = base_file_path + ".json"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        content = json.load(f)
        print(content)

with open(file_path, 'w') as f:
    json.dump(list(range(11)), f, indent=4)

if os.path.exists(folder_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    os.removedirs(folder_path)
