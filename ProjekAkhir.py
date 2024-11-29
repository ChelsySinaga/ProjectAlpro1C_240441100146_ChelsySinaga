class KeuanganPribadi:
    def __init__(self):
        self.transaksi = []

    def tambah_transaksi(self, jenis, jumlah, deskripsi):
        self.transaksi.append({
            'jenis': jenis,
            'jumlah': jumlah,
            'deskripsi': deskripsi
        })

    def tampilkan_transaksi(self):
        print("\nTransaksi Keuangan:")
        if not self.transaksi:
            print("Tidak ada transaksi.")
            return
        for idx, t in enumerate(self.transaksi):
            print(f"{idx + 1}. {t['jenis']} - {t['jumlah']} - {t['deskripsi']}")

    def total_pemasukan(self):
        total = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'pemasukan')
        return total

    def total_pengeluaran(self):
        total = sum(t['jumlah'] for t in self.transaksi if t['jenis'] == 'pengeluaran')
        return total

    def saldo(self):
        return self.total_pemasukan() - self.total_pengeluaran()

    def kategori_transaksi(self):
        kategori = {}
        for t in self.transaksi:
            if t['jenis'] not in kategori:
                kategori[t['jenis']] = []
            kategori[t['jenis']].append(t['jumlah'])
        return kategori


def main():
    keuangan = KeuanganPribadi()

    while True:
        print("\nMenu:")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Transaksi")
        print("4. Tampilkan Total Pemasukan")
        print("5. Tampilkan Total Pengeluaran")
        print("6. Tampilkan Saldo")
        print("7. Tampilkan Kategori Transaksi")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            jumlah = float(input("Masukkan jumlah pemasukan: "))
            deskripsi = input("Masukkan deskripsi: ")
            keuangan.tambah_transaksi('pemasukan', jumlah, deskripsi)
        elif pilihan == '2':
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            deskripsi = input("Masukkan deskripsi: ")
            keuangan.tambah_transaksi('pengeluaran', jumlah, deskripsi)
        elif pilihan == '3':
            keuangan.tampilkan_transaksi()
        elif pilihan == '4':
            print(f"Total Pemasukan: {keuangan.total_pemasukan()}")
        elif pilihan == '5':
            print(f"Total Pengeluaran: {keuangan.total_pengeluaran()}")
        elif pilihan == '6':
            print(f"Saldo: {keuangan.saldo()}")
        elif pilihan == '7':
            kategori = keuangan.kategori_transaksi()
            for jenis, jumlah in kategori.items():
                print(f"{jenis.capitalize()}: {sum(jumlah)}")
        elif pilihan == '8':
            print("Terima kasih! Selamat tinggal.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()