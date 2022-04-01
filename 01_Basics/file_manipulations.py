# Input/Output de fichiers texte
myfile = open("text.txt")
print(f"Première lecture : {myfile.read()}")
print(f"Seconde lecture : {myfile.read()}")
myfile.seek(0)
print(f"Après reset du curseur : {myfile.read()}")
myfile.seek(0)
print(f"Après reset du curseur : {myfile.readlines()}")
myfile.close()

# Version qui permet la fermeture automatiquement
with open("text2.txt", mode='w') as my_writed_file:
    my_writed_file.write("Hello it's me")
with open("text2.txt", mode='a') as appending_to_file:
    appending_to_file.write("\nI'm new")
with open("text2.txt", mode='r') as my_new_file:
    content_of_file = my_new_file.read()
print(f"Content of file : {content_of_file}")