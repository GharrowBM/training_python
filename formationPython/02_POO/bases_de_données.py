import sqlite3, os
from mes_constantes import DATA_DIR

db_path = os.path.join(DATA_DIR, "database.db")

with sqlite3.connect(db_path) as conn:
    c = conn.cursor()

    # CREATE TABLE - Création de la table (si non existante)
    # Trois guillemets permettent une string multi-lignes
    # c.execute("""CREATE TABLE IF NOT EXISTS dogs(
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 name VARCHAR (50),
    #                 breed VARCHAR (50),
    #                 age INTEGER
    #             )""")

    # INSERT - Ajout de valeurs dans la table
    # d = {'a': "Rye", 'b': "Husky", 'c': 4}
    # c.execute("INSERT INTO dogs (name, breed, age) VALUES (:a, :b, :c)", d)

    # SELECT - Lecture des valeurs dans la table
    # c.execute("SELECT * FROM dogs")
    # first_data = c.fetchone()
    # print(first_data)
    # datas = c.fetchall()
    # for index, item in enumerate(datas):
    #     print(f"{index}: {item}")

    # UPDATE - Modifier valeurs dans la table
    # d = {'a': "Candy", 'b': "Chihuahua", 'c': 3}
    # c.execute("""UPDATE dogs SET name=:a, breed=:b, age=:c WHERE id=2""", d)

    # DELETE - Supprimer des données dans la table
    # c.execute("""DELETE FROM dogs WHERE id=2""", d)

    conn.commit()
