#TUGAS NO 2

class Buku :
    def __init__(self, title) :
        self.title = title
        self.next_book = None

class Pengunjung :
    def __init__(self, name) :
        self.name = name
        self.borrowed_books = None 

    def Jenis_Buku (self, title) :
        buku_baru = Buku (title) 
        if self.borrowed_books is None :
            self.borrowed_books = buku_baru
        else :
            current_book = self.borrowed_books
            while current_book.next_book is not None :
                current_boook = current_book.next_book
            current_book.next_book = buku_baru 
    
    def print_borrowed_books (self) :
        if self.borrowed_books is None :
            print ("Tidak ada buku yang dipijam", self.name)
        else :
            print ("Buku yang dipinjam", self.name, ":")
            current_book = self.borrowed_books
            while current_book is not None :
                print (" ", current_book.title)
                current_book = current_book.next_book

Pengunjung1 = Pengunjung ("John")
Pengunjung1.Jenis_Buku ("Judul Buku : " "Harry Potter")
Pengunjung1.Jenis_Buku ("----------------------------------------")

Pengunjung2 = Pengunjung ("Jane")
Pengunjung2.Jenis_Buku ("Judul Buku : " "To Kill a Mockingbird")
Pengunjung2.Jenis_Buku ("----------------------------------------")

Pengunjung3 = Pengunjung ("Mike")
Pengunjung3.Jenis_Buku ("Judul Buku : " "The Great Gatsby")
Pengunjung3.Jenis_Buku ("----------------------------------------")

Pengunjung4 = Pengunjung ("Sarah")
Pengunjung4.Jenis_Buku ("Judul Buku : " "Pride and Prejudice")
Pengunjung4.Jenis_Buku ("----------------------------------------")

Pengunjung1.print_borrowed_books ()
Pengunjung2.print_borrowed_books ()
Pengunjung3.print_borrowed_books ()
Pengunjung4.print_borrowed_books ()