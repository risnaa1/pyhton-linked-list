class Pemain:
    def __init__(self, nama, ranking):
        self.name = nama
        self.ranking = ranking
        self.next_partisipasi = None


class Turnamen:
    def __init__(self):
        self.head = None

    def registasi_pemain(self, nama, ranking):
        pemain_baru = Pemain (nama, ranking)
        if self.head is None:
            self.head = pemain_baru
        else:
            current_partisipasi = self.head
            while current_partisipasi.next_partisipasi is not None:
                current_partisipasi = current_partisipasi.next_partisipasi
            current_partisipasi.next_partisipasi= pemain_baru

    def eliminasi_pemain(self, nama):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        if self.head.name == nama:
            self.head = self.head.next_partisipasi
            print("Peserta", nama, "telah dieliminasi.")
            return

        current_partisipasi = self.head
        prev_participant = None
        while current_partisipasi is not None:
            if current_partisipasi.name == nama:
                prev_participant.next_partisipasi= current_partisipasi.next_partisipasi
                print("Peserta", nama, "telah dieliminasi.")
                return
            prev_participant = current_partisipasi
            current_partisipasi = current_partisipasi.next_partisipasi

        print("Peserta", nama, "tidak ditemukan.")

    def print_partisipasi_by_ranking(self):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        sorted_participants = self._sort_partisipasi_by_ranking()
        print("Daftar peserta berdasarkan peringkat:")
        for participant in sorted_participants:
            print("Nama         :", participant.name) 
            print("Peringkat    :", participant.ranking)
            print("---------------------------------------------")

    def _sort_partisipasi_by_ranking(self):
        participants = []
        current_partisipasi = self.head
        while current_partisipasi is not None:
            participants.append(current_partisipasi)
            current_partisipasi = current_partisipasi.next_partisipasi
        participants.sort(key=lambda x: x.ranking)
        return participants


# Contoh penggunaan program
turnamen = Turnamen()

turnamen.registasi_pemain("Udin", 1500)
turnamen.registasi_pemain("Epul", 1700)
turnamen.registasi_pemain("Jana", 1000)
turnamen.registasi_pemain("Odang", 1800)

turnamen.print_partisipasi_by_ranking()

turnamen.eliminasi_pemain ("Jana")

turnamen.print_partisipasi_by_ranking()
