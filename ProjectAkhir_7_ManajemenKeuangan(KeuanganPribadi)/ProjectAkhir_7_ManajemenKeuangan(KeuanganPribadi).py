# Program Laporan Keuangan Sederhana dengan Algoritma Penanggalan
# Variabel untuk menyimpan riwayat transaksi
riwayat = {}
pengeluaran_total=0
pemasukan_total=0
tabungan=0
# Fungsi penanggalan
jumlah_bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def cek_kabisat(tahun):
    """Cek apakah tahun adalah tahun kabisat"""
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def get_hari_per_bulan(tahun):
    """Mengembalikan list jumlah hari per bulan untuk tahun tertentu"""
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if cek_kabisat(tahun):
        hari_per_bulan[1] = 29  # Februari menjadi 29 hari
    return hari_per_bulan

# Input tanggal awal dan akhir
print("=== Input Tanggal Mulai ===")
while True:
    try:
        tahun_awal = int(input("Masukkan Tahun: "))
        if tahun_awal < 0 or tahun_awal == 0:
            print("Tidak boleh negatif / tidak boleh 0")
        else:
            break
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")

while True:
    try:
        input_bulan = int(input("Bulan (1-12): "))
        if input_bulan < 0:
            print("Tidak boleh negatif")
        elif input_bulan > 12:
            print("Inputan bulan melebihi batas")
        else:
            break
    except ValueError:
        print("Bulan tidak masuk kriteria!!!")

while True:
    try:
        input_hari = int(input("Tanggal (1-31): "))
        if input_hari < 0:
            print("Tidak boleh negatif")
        elif input_hari > 31:
            print("Tanggal melebihi")
        else:
            break
    except ValueError:
        print("Tanggal tidak masuk kriteria!!!")

print("==JANGKA WAKTU LAPORAN==")
print("    1. Per tahun        ")
print("    2. Per bulan        ")
print("    3. Per Minggu       ")
while True:
    try:
        input_jangka = int(input("Pilihan (1-3): "))
        if input_jangka < 0:
            print("Tidak boleh negatif")
        elif input_jangka > 3:
            print("Pilihan melebihi")
        else:
            break
    except ValueError:
        print("Tidak valid")

# Inisialisasi variabel
if input_jangka == 1:
    print("Jangka waktu laporan per tahun")
    batas_hari = 366 if cek_kabisat(tahun_awal) else 365
elif input_jangka == 2:
    print("Jangka waktu laporan per bulan")
    batas_hari = 30
elif input_jangka == 3:
    print("Jangka waktu laporan per minggu")
    batas_hari = 7

hari_tercetak = 0
tahun_sekarang = tahun_awal
bulan_index = input_bulan - 1

print(f"\nMemulai dari tahun {tahun_awal}")
if cek_kabisat(tahun_awal):
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")
print(f"Total hari dalam jangka waktu: {batas_hari}")
print("="*50)

# Fungsi untuk menghitung saldo saat ini
def hitung_saldo_saat_ini(tanggal_format):
    """Hitung saldo kas sampai tanggal tertentu"""
    saldo = 0
    for tgl in riwayat:
        # Hanya hitung tanggal yang <= tanggal_format
        tgl_parts = tgl.split('/')
        current_parts = tanggal_format.split('/')
        
        # Konversi ke angka untuk perbandingan
        tgl_hari, tgl_bulan, tgl_tahun = int(tgl_parts[0]), int(tgl_parts[1]), int(tgl_parts[2])
        curr_hari, curr_bulan, curr_tahun = int(current_parts[0]), int(current_parts[1]), int(current_parts[2])
        
        # Cek jika tanggal ini <= tanggal yang diminta
        if (tgl_tahun < curr_tahun) or \
           (tgl_tahun == curr_tahun and tgl_bulan < curr_bulan) or \
           (tgl_tahun == curr_tahun and tgl_bulan == curr_bulan and tgl_hari <= curr_hari):
            
            for tr in riwayat[tgl]:
                if tr['jenis'] == "Pemasukan":
                    saldo += tr['nominal']
                else:
                    saldo -= tr['nominal']
    
    return saldo

# Looping berdasarkan algoritma penanggalan
while hari_tercetak < batas_hari:
    # Perbarui hari_per_bulan untuk tahun sekarang
    hari_per_bulan_sekarang = get_hari_per_bulan(tahun_sekarang)
    
    # Hitung indeks bulan yang benar
    bulan_aktual = bulan_index % 12
    bulan = jumlah_bulan[bulan_aktual]
    
    # Jika bulan_index melebihi 11, artinya tahun berganti
    if bulan_index >= 12:
        tahun_sekarang += 1
        bulan_index = 0
        bulan_aktual = 0
        hari_per_bulan_sekarang = get_hari_per_bulan(tahun_sekarang)
        print(f"\n{'='*50}")
        print(f"PINDAH KE TAHUN {tahun_sekarang}")
        if cek_kabisat(tahun_awal):
            print("Tahun kabisat")
        else:
            print("Bukan tahun kabisat")
        print(f"Total hari dalam jangka waktu: {batas_hari}")
        print("="*50)
        print(f"{'='*50}")
    
    # Tentukan tanggal mulai
    if hari_tercetak == 0:
        tanggal_mulai = input_hari
    else:
        tanggal_mulai = 1
    
    # Loop untuk setiap hari dalam bulan
    for tanggal in range(tanggal_mulai, hari_per_bulan_sekarang[bulan_aktual] + 1):
        tanggal_format = f"{tanggal:02d}/{bulan:02d}/{tahun_sekarang}"
        if tanggal_format not in riwayat:
            riwayat[tanggal_format] = []
        
        # Menu transaksi harian
        while True:
            saldo_kas_sekarang = hitung_saldo_saat_ini(tanggal_format)
            
            print(f"\n{'='*50}")
            print(f"TANGGAL: {tanggal_format}")
            print(f"{'='*50}")
            print(f"💰 Saldo Kas:  Rp {saldo_kas_sekarang:,}")
            print(f"TABUNGAN ANDA SEKARANG: Rp {tabungan:,}")
            print(f"{'='*50}")
            print("Menu Transaksi:")
            print("1. Pemasukan")
            print("2. Pengeluaran")
            print("3. Lihat riwayat transaksi hari ini")
            print("4. Lanjut ke hari berikutnya")
            print("5. Keluar dari program (selesai lebih awal)")
            print("6. Menabung ")
            print("="*50)

            pilihan = input("Pilih menu (1-6): ")

            if pilihan == "1":
                # Pemasukan
                print("\nKategori Pemasukan:")
                print("1. Gaji")
                print("2. Lainnya")
                print("3. Kembali")
                while True:
                    try:
                        kategori_input = int(input("Pilih kategori (1/2/3): "))
                        if kategori_input < 0:
                            print("Tidak boleh negatif")
                        else:
                            break
                    except ValueError:
                        print("Harus angka")
                
                if kategori_input == 1:
                    kategori = "Gaji"
                elif kategori_input == 2:
                    kategori = "Lainnya"
                elif kategori_input == 3:
                    print("Kembali ke menu utama")
                    continue
                else:
                    print("Kategori tidak valid!")
                    continue
                
                while True:
                    try:
                        nominal = int(input(f"Masukkan nominal pemasukan ({kategori}): Rp "))
                        if nominal < 0:
                            print("Tidak boleh minus")
                        else:
                            break
                    except ValueError:
                        print("Harus angka!")
                
                catatan = input("Catatan transaksi: ")
                yakin = input("Apakah yakin menyimpan? (y/n): ")
                if yakin.lower() == "y":
                    riwayat[tanggal_format].append({
                        "jenis": "Pemasukan",
                        "kategori": kategori,
                        "nominal": nominal,
                        "catatan": catatan
                    })
                    print("✅ Transaksi pemasukan tersimpan!")
                    pemasukan_total+=nominal
                else:
                    print("Transaksi dibatalkan!")

            elif pilihan == "2":
                # Pengeluaran
                print("\nKategori Pengeluaran:")
                print("1. Kebutuhan Pokok")
                print("2. Lainnya")
                print("3. Kembali")
                while True:
                    try:
                        kategori_input = int(input("Pilih kategori (1/2/3): "))
                        if kategori_input < 0:
                            print("Tidak boleh negatif")
                        else:
                            break
                    except ValueError:
                        print("Harus angka")
                
                if kategori_input == 1:
                    kategori = "Kebutuhan Pokok"
                elif kategori_input == 2:
                    kategori = "Lainnya"
                elif kategori_input == 3:
                    print("Kembali ke menu utama")
                    continue
                else:
                    print("Kategori tidak valid!")
                    continue
                
                # Hitung saldo kas saat ini sebelum pengeluaran
                saldo_kas_sebelum = hitung_saldo_saat_ini(tanggal_format)
                
                while True:
                    while True:
                        try:
                            nominal = int(input(f"Masukkan nominal pengeluaran ({kategori}): Rp "))
                            perisai_tabungan=saldo_kas_sebelum-saldo_kas_sebelum
                            if perisai_tabungan==tabungan or perisai_tabungan<tabungan:
                                print("anda melebihi pengeluaran karena terhalang tabungan")
                                break
                            elif nominal < 0:
                                print("Inputan tidak boleh kurang dari 0")
                            else:
                                break
                        except ValueError:
                            print("Harus angka !!")
                    
                    # VALIDASI: Cek apakah pengeluaran melebihi saldo kas
                    if nominal > saldo_kas_sebelum :
                        print(f"\n❌ SALDO KAS TIDAK CUKUP!")
                        print(f"   Saldo kas saat ini: Rp {saldo_kas_sebelum:,}")
                        
                        ulangi = input("Apakah ingin menginput ulang dengan nominal lain? (y/n): ")
                        if ulangi.lower() != 'y':
                            print("Transaksi dibatalkan!")
                            break
                    else:
                        # Saldo mencukupi, lanjut ke catatan
                        catatan = input("Catatan transaksi: ")
                        yakin = input("Apakah yakin menyimpan? (y/n): ")
                        
                        if yakin.lower() == "y":
                            riwayat[tanggal_format].append({
                                "jenis": "Pengeluaran",
                                "kategori": kategori,
                                "nominal": nominal,
                                "catatan": catatan
                            })
                            print("✅ Transaksi tersimpan!")
                            pengeluaran_total+=nominal
                        else:
                            print("Transaksi dibatalkan!")
                        break  # Keluar dari loop validasi
                continue

            elif pilihan == "3":
                # Lihat riwayat transaksi hari ini
                if not riwayat[tanggal_format]:
                    print("Belum ada transaksi hari ini.")
                else:
                    print(f"\n{'='*50}")
                    print(f"RIWAYAT TRANSAKSI - {tanggal_format}")
                    print(f"{'='*50}")
                    total_pemasukan = 0
                    total_pengeluaran = 0
                    
                    for idx, tr in enumerate(riwayat[tanggal_format], 1):
                        if tr['jenis'] == "Pemasukan":
                            tanda = "[+]"
                        else:
                            tanda = "[-]"
                        
                        print(f"{idx}. {tanda} {tr['jenis']} - {tr['kategori']} - Rp {tr['nominal']:,}")
                        print(f"   Catatan: {tr['catatan']}")
                        
                        if tr['jenis'] == "Pemasukan":
                            total_pemasukan += tr['nominal']
                        else:
                            total_pengeluaran += tr['nominal']
                    
                    saldo_hari_ini = total_pemasukan - total_pengeluaran
                    
                    print(f"\n{'='*40}")
                    print(f"Total Pemasukan Hari Ini:  Rp {total_pemasukan:,}")
                    print(f"Total Pengeluaran Hari Ini: Rp {total_pengeluaran:,}")
                    print(f"Saldo Hari Ini:            Rp {saldo_hari_ini:,}")
                    print(f"{'='*40}")

            elif pilihan == "4":
                print("Lanjut ke hari berikutnya...")
                break

            elif pilihan == "5":
                print("Keluar dari program...")
                # Hitung hari yang sudah dicetak
                hari_tercetak = batas_hari  # Force exit
                break
            elif pilihan=="6":
                print("========selamat datang di fitur tabungan==============")
                print("                       deskripsi                      ")
                print("|Di fitur ini menabung adalah opsional,menabung dapat|")
                print("| di lakukan dengan nominal paling kecil 1 rupiah!!  |")
                print()
                print("|| TABUNGAN TIDAK BISA DI AMBIL PADA SAAT BELUM MENCAPAI BATAS WAKTU || ")
                while True:
                    try:
                        nominal_tabung=int(input("input jumlah tabungan / PENCET  1 UNTUK KEMBALI KE MENU =  "))
                        if nominal_tabung<0:
                            print("inputan tidak boleh negatif ")
                        elif nominal_tabung == 1 :
                            print("Kembali ke menu utama")
                            print()
                            break
                        elif nominal_tabung>saldo_kas_sekarang:
                            print("inputan melebihi saldo yang ada")
                        else:
                            break
                    except ValueError:
                        print("harus angka!!!")        
                tabungan=tabungan+nominal_tabung
            else:
                print("Pilihan tidak valid!")
        
        hari_tercetak += 1
        
        # Berhenti jika sudah mencapai batas
        if hari_tercetak >= batas_hari:
            break
    
    bulan_index += 1

print()
print(f"==========RINGKASAN TRANSAKSI SELAMA {batas_hari} HARI ============")
print(f"HASIL TABUNGAN TABUNG = {tabungan:,}")
print(f"PEMASUKAN TOTAL       = {pemasukan_total:,}")
print(f"PENGELUARAN TOTAL     = {pengeluaran_total:,} ")
for tanggal in riwayat:  
    print(f"CATATAN TRANSAKSI TANGGAL: {tanggal}")
    print("=" * 50)
    
    # Cek apakah ada transaksi di tanggal ini
    if len(riwayat[tanggal]) == 0:
        print("Tidak ada catatan transaksi")
        continue
    
    # Loop melalui semua transaksi di tanggal tersebut
    for i in range(len(riwayat[tanggal])):
        tr = riwayat[tanggal][i]  # Ambil transaksi ke-i
        print(f"{i}. {tr['jenis']} - {tr['kategori']} - Rp {tr['nominal']:,}")
        print(f"   Catatan: {tr['catatan']}")