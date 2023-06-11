class Produk:
    def __init__(self, nama, kode, stok):
        self.nama = nama
        self.code = kode
        self.stock = stok
        self.next = None


class PersediaanManajemen:
    def __init__(self):
        self.head = None

    def tambah_produk(self, nama, kode, stok):
        produk_baru = Produk (nama, kode, stok)
        if self.head is None:
            self.head = produk_baru
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = produk_baru

    def hapus_produk(self, kode):
        if self.head is None:
            return

        if self.head.code == kode:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.code == kode:
                current.next = current.next.next
                return
            current = current.next

    def print_inventaris (self):
        if self.head is None:
            print("Tidak ada inventaris")
            return

        print("Daftar produk dalam inventaris :")
        current = self.head
        while current is not None:
            print ("Nama        :", current.nama)
            print ("Kode        :",current.code) 
            print ("Jumlah Stok :", current.stock)
            print ("-------------------------------")
            current = current.next



inventaris = PersediaanManajemen()

inventaris.tambah_produk("Kemeja", "AA001", 20)
inventaris.tambah_produk("Kaos", "SS004", 10)
inventaris.tambah_produk("Sepatu", "DD001", 40)
inventaris.tambah_produk("Sendal", "YY006", 20)

inventaris.print_inventaris()

inventaris.hapus_produk("YY006")

inventaris.print_inventaris()
