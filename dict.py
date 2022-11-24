import psycopg2

#Jag hade redan ändrat från C till conn
def get_db_connection():
    conn = psycopg2.connect(
            user="postgres",
            password="5731",
            host="localhost",
            port="5432",
            database="dict_db")
    return conn
#gives the list
def read_dict():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
#adds words and their translation
def add_word(word, translation):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
    conn.close()
#deletes!
def delete_word(ID):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
    conn.close()
#saves
def save_dict():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

while True: ## REPL - Read Execute Program Loop
    print("Welcome! \nTo use the dictionary, use the following commands: list, add, delete and quit. "
    "\nHave fun!")
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict())
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(word, translation)
        print(f" Added word {word}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(ID)
    elif cmd == "quit":
        save_dict()
        print("Bye bye!")
        exit()
