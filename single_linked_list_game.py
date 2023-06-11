class Item:
    def __init__(self, nama, kepentingan):
        self.name = nama
        self.importance = kepentingan
        self.next_item = None


class Investasi:
    def __init__(self):
        self.head = None

    def tambah_item(self, nama, kepentingan):
        item_baru = Item(nama, kepentingan)
        if self.head is None:
            self.head = item_baru
        else:
            current_item = self.head
            while current_item.next_item is not None:
                current_item = current_item.next_item
            current_item.next_item = item_baru

    def remove_item(self, nama):
        if self.head is None:
            print("Tas ini tidak ada apa-apanya")
            return

        if self.head.name == nama:
            self.head = self.head.next_item
            print("Item", nama, "sudah dihapus")
            return

        current_item = self.head
        prev_item = None
        while current_item is not None:
            if current_item.name == nama:
                prev_item.next_item = current_item.next_item
                print("Item", nama, "sudah dihapus")
                return
            prev_item = current_item
            current_item = current_item.next_item

        print("Item", nama, "tidak ditemukan")

    def print_items_by_importance(self):
        if self.head is None:
            print("Tas ini tidak ada apa-apanya")
            return

        sorted_items = self._sort_items_by_importance()
        print("Daftar item dalam tas berdasarkan tingkat kepentingannya :")
        for item in sorted_items:
            print ("Nama        :", item.name) 
            print ("Kepentingan :", item.importance)

    def _sort_items_by_importance(self):
        items = []
        current_item = self.head
        while current_item is not None:
            items.append(current_item)
            current_item = current_item.next_item
        items.sort(key=lambda x: x.importance, reverse=True)
        return items


inventory = Investasi()

inventory.tambah_item("Armor", 10)
inventory.tambah_item("Petak Umpet", 5)
inventory.tambah_item("Pedang", 4)
inventory.tambah_item("Mencuri Emas", 2)

inventory.print_items_by_importance()

inventory.remove_item("Petak Umpet")

inventory.print_items_by_importance()