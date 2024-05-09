import sqlite3
from tkinter import *
from tkinter import messagebox

def create_database():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    # Таблица "Авторы"
    c.execute('''CREATE TABLE IF NOT EXISTS Authors
                 (author_id INTEGER PRIMARY KEY,
                 author_name TEXT NOT NULL,
                 birth_date DATE)''')

    # Таблица "Жанры"
    c.execute('''CREATE TABLE IF NOT EXISTS Genres
                 (genre_id INTEGER PRIMARY KEY,
                 genre_name TEXT NOT NULL)''')

    # Таблица "Книги"
    c.execute('''CREATE TABLE IF NOT EXISTS Books
                 (book_id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 publication_date DATE,
                 author_id INTEGER,
                 genre_id INTEGER,
                 FOREIGN KEY (author_id) REFERENCES Authors(author_id),
                 FOREIGN KEY (genre_id) REFERENCES Genres(genre_id))''')

    conn.commit()
    conn.close()

def insert_data(table_name, data):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    try:
        if table_name == 'Authors':
            c.execute("INSERT INTO Authors (author_name, birth_date) VALUES (?, ?)", data)
        elif table_name == 'Genres':
            c.execute("INSERT INTO Genres (genre_name) VALUES (?)", data)
        elif table_name == 'Books':
            c.execute("INSERT INTO Books (title, publication_date, author_id, genre_id) VALUES (?, ?, ?, ?)", data)
        conn.commit()
        messagebox.showinfo("Успех", "Данные успешно добавлены!")
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", str(e))
    finally:
        conn.close()

def update_data(table_name, data):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    try:
        if table_name == 'Authors':
            c.execute("UPDATE Authors SET author_name = ?, birth_date = ? WHERE author_id = ?", data)
        elif table_name == 'Genres':
            c.execute("UPDATE Genres SET genre_name = ? WHERE genre_id = ?", data)
        elif table_name == 'Books':
            c.execute("UPDATE Books SET title = ?, publication_date = ?, author_id = ?, genre_id = ? WHERE book_id = ?", data)
        conn.commit()
        messagebox.showinfo("Успех", "Данные успешно обновлены!")
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", str(e))
    finally:
        conn.close()

def delete_all_data():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM Authors")
        c.execute("DELETE FROM Genres")
        c.execute("DELETE FROM Books")
        conn.commit()
        messagebox.showinfo("Успех", "Все данные успешно удалены!")
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", str(e))
    finally:
        conn.close()

def display_data():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    # Получение данных из таблицы Авторы
    c.execute("SELECT * FROM Authors")
    authors = c.fetchall()

    # Получение данных из таблицы Жанры
    c.execute("SELECT * FROM Genres")
    genres = c.fetchall()

    # Получение данных из таблицы Книги
    c.execute("SELECT Books.book_id, Books.title, Books.publication_date, Authors.author_name, Genres.genre_name FROM Books \
               INNER JOIN Authors ON Books.author_id = Authors.author_id \
               INNER JOIN Genres ON Books.genre_id = Genres.genre_id")
    books = c.fetchall()

    conn.close()

    # Отображение данных в текстовом поле
    display_window = Tk()
    display_window.title("Отображение данных")

    display_text = Text(display_window)
    display_text.pack()

    # Отображение данных об авторах
    display_text.insert(END, "Авторы:\n")
    for author in authors:
        display_text.insert(END, f"ID: {author[0]}, Имя: {author[1]}, Дата рождения: {author[2]}\n")

    # Отображение данных о жанрах
    display_text.insert(END, "\nЖанры:\n")
    for genre in genres:
        display_text.insert(END, f"ID: {genre[0]}, Название: {genre[1]}\n")

    # Отображение данных о книгах
    display_text.insert(END, "\nКниги:\n")
    for book in books:
        display_text.insert(END, f"ID: {book[0]}, Название: {book[1]}, Дата публикации: {book[2]}, Автор: {book[3]}, Жанр: {book[4]}\n")

    display_text.config(state=DISABLED)  # Запретить редактирование текстового поля

    display_window.mainloop()

def main():
    def add_author():
        name = author_name.get()
        birth_date = author_birth_date.get()
        insert_data('Authors', (name, birth_date))
        author_name.delete(0, END)
        author_birth_date.delete(0, END)

    def add_genre():
        genre_name_val = genre_name.get()
        insert_data('Genres', (genre_name_val,))
        genre_name.delete(0, END)

    def add_book():
        title_val = book_title.get()
        pub_date_val = publication_date.get()
        author_id_val = author_id.get()
        genre_id_val = genre_id.get()
        insert_data('Books', (title_val, pub_date_val, author_id_val, genre_id_val))
        book_title.delete(0, END)
        publication_date.delete(0, END)
        author_id.delete(0, END)
        genre_id.delete(0, END)

    def update_author():
        author_id_val = update_author_id.get()
        name_val = update_author_name.get()
        birth_date_val = update_author_birth_date.get()
        update_data('Authors', (name_val, birth_date_val, author_id_val))

    def update_genre():
        genre_id_val = update_genre_id.get()
        name_val = update_genre_name.get()
        update_data('Genres', (name_val, genre_id_val))

    def update_book():
        book_id_val = update_book_id.get()
        title_val = update_book_title.get()
        pub_date_val = update_publication_date.get()
        author_id_val = update_author_id.get()
        genre_id_val = update_genre_id.get()
        update_data('Books', (title_val, pub_date_val, author_id_val, genre_id_val, book_id_val))

    def delete_all():
        confirm = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить все данные?")
        if confirm:
            delete_all_data()

    root = Tk()
    root.title("Система управления библиотекой")
    root.configure(background='plum3')
    
    # Элементы интерфейса для добавления авторов
    author_name_label = Label(root, text="Имя автора:")
    author_name_label.grid(row=0, column=0, padx=10, pady=5)
    author_name = Entry(root)
    author_name.grid(row=0, column=1, padx=10, pady=5)

    author_birth_date_label = Label(root, text="Дата рождения:")
    author_birth_date_label.grid(row=1, column=0, padx=10, pady=5)
    author_birth_date = Entry(root)
    author_birth_date.grid(row=1, column=1, padx=10, pady=5)

    add_author_button = Button(root, text="Добавить автора", command=add_author)
    add_author_button.grid(row=2, columnspan=2, padx=10, pady=10)

    # Элементы интерфейса для добавления жанров
    genre_name_label = Label(root, text="Название жанра:")
    genre_name_label.grid(row=3, column=0, padx=10, pady=5)
    genre_name = Entry(root)
    genre_name.grid(row=3, column=1, padx=10, pady=5)

    add_genre_button = Button(root, text="Добавить жанр", command=add_genre)
    add_genre_button.grid(row=4, columnspan=2, padx=10, pady=10)

    # Элементы интерфейса для добавления книг
    book_title_label = Label(root, text="Название книги:")
    book_title_label.grid(row=5, column=0, padx=10, pady=5)
    book_title = Entry(root)
    book_title.grid(row=5, column=1, padx=10, pady=5)

    publication_date_label = Label(root, text="Дата публикации:")
    publication_date_label.grid(row=6, column=0, padx=10, pady=5)
    publication_date = Entry(root)
    publication_date.grid(row=6, column=1, padx=10, pady=5)

    author_id_label = Label(root, text="ID автора:")
    author_id_label.grid(row=7, column=0, padx=10, pady=5)
    author_id = Entry(root)
    author_id.grid(row=7, column=1, padx=10, pady=5)

    genre_id_label = Label(root, text="ID жанра:")
    genre_id_label.grid(row=8, column=0, padx=10, pady=5)
    genre_id = Entry(root)
    genre_id.grid(row=8, column=1, padx=10, pady=5)

    add_book_button = Button(root, text="Добавить книгу", command=add_book)
    add_book_button.grid(row=9, columnspan=2, padx=10, pady=10)

    # Элементы интерфейса для обновления информации
    update_author_id_label = Label(root, text="ID автора для обновления:")
    update_author_id_label.grid(row=10, column=0, padx=10, pady=5)
    update_author_id = Entry(root)
    update_author_id.grid(row=10, column=1, padx=10, pady=5)

    update_author_name_label = Label(root, text="Новое имя автора:")
    update_author_name_label.grid(row=11, column=0, padx=10, pady=5)
    update_author_name = Entry(root)
    update_author_name.grid(row=11, column=1, padx=10, pady=5)

    update_author_birth_date_label = Label(root, text="Новая дата рождения:")
    update_author_birth_date_label.grid(row=12, column=0, padx=10, pady=5)
    update_author_birth_date = Entry(root)
    update_author_birth_date.grid(row=12, column=1, padx=10, pady=5)

    update_author_button = Button(root, text="Обновить информацию об авторе", command=update_author)
    update_author_button.grid(row=13, columnspan=2, padx=10, pady=10)

    update_genre_id_label = Label(root, text="ID жанра для обновления:")
    update_genre_id_label.grid(row=14, column=0, padx=10, pady=5)
    update_genre_id = Entry(root)
    update_genre_id.grid(row=14, column=1, padx=10, pady=5)

    update_genre_name_label = Label(root, text="Новое название жанра:")
    update_genre_name_label.grid(row=15, column=0, padx=10, pady=5)
    update_genre_name = Entry(root)
    update_genre_name.grid(row=15, column=1, padx=10, pady=5)

    update_genre_button = Button(root, text="Обновить информацию о жанре", command=update_genre)
    update_genre_button.grid(row=16, columnspan=2, padx=10, pady=10)

    update_book_id_label = Label(root, text="ID книги для обновления:")
    update_book_id_label.grid(row=17, column=0, padx=10, pady=5)
    update_book_id = Entry(root)
    update_book_id.grid(row=17, column=1, padx=10, pady=5)

    update_book_title_label = Label(root, text="Новое название книги:")
    update_book_title_label.grid(row=18, column=0, padx=10, pady=5)
    update_book_title = Entry(root)
    update_book_title.grid(row=18, column=1, padx=10, pady=5)

    update_publication_date_label = Label(root, text="Новая дата публикации:")
    update_publication_date_label.grid(row=19, column=0, padx=10, pady=5)
    update_publication_date = Entry(root)
    update_publication_date.grid(row=19, column=1, padx=10, pady=5)

    update_author_id_label_2 = Label(root, text="Новый ID автора:")
    update_author_id_label_2.grid(row=20, column=0, padx=10, pady=5)
    update_author_id_2 = Entry(root)
    update_author_id_2.grid(row=20, column=1, padx=10, pady=5)

    update_genre_id_label_2 = Label(root, text="Новый ID жанра:")
    update_genre_id_label_2.grid(row=21, column=0, padx=10, pady=5)
    update_genre_id_2 = Entry(root)
    update_genre_id_2.grid(row=21, column=1, padx=10, pady=5)

    update_book_button = Button(root, text="Обновить информацию о книге", command=update_book)
    update_book_button.grid(row=22, columnspan=2, padx=10, pady=10)

    delete_all_button = Button(root, text="Удалить все данные", command=delete_all)
    delete_all_button.grid(row=23, columnspan=2, padx=10, pady=10)

    display_button = Button(root, text="Отобразить данные", command=display_data)
    display_button.grid(row=24, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_database()
    main()
