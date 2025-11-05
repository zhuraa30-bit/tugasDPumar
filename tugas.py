import sys
import os

GAJI_POKOK = 300000

def hitung_tunjangan_jabatan(golongan: int) -> int:
    """Menghitung Tunjangan Jabatan berdasarkan Golongan (1, 2, 3)."""
    
    PERSENTASE_JABATAN = {
        1: 0.05,
        2: 0.10,
        3: 0.15
    }
    persen = PERSENTASE_JABATAN.get(golongan, 0.0)
    return int(persen * GAJI_POKOK)
def hitung_tunjangan_pendidikan(pendidikan: str) -> int:
    """Menghitung Tunjangan Pendidikan berdasarkan Tingkat Pendidikan."""
    pendidikan = pendidikan.upper()
    PERSENTASE_PENDIDIKAN = {
        "SMA": 0.025,
        "D1":  0.05,
        "D3":  0.20,
        "S1":  0.30
    }
    
    persen = PERSENTASE_PENDIDIKAN.get(pendidikan, 0.0)
    return int(persen * GAJI_POKOK)
def hitung_honor_lembur(jam_kerja: int) -> int:
    """Menghitung Honor Lembur jika jam kerja > 8 jam."""
    
    JAM_NORMAL = 8
    HONOR_PER_JAM_LEMBUR = 3500
    
    if jam_kerja > JAM_NORMAL:
        jam_lembur = jam_kerja - JAM_NORMAL
        return jam_lembur * HONOR_PER_JAM_LEMBUR
    else:
        return 0
def format_rupiah(angka: int) -> str:
    """Helper untuk format angka ke string Rupiah."""
    return f"Rp {angka:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
def main():
    print("=" * 42)
    print("   PROGRAM HITUNG GAJI KARYAWAN KONTRAK   ")
    print("        PT. DINGIN DAMAI (Kontrak)        ")
    print("=" * 42)
    print(f"Gaji Pokok: {format_rupiah(GAJI_POKOK)} per bulan")
    print("-" * 42)
    try:
        nama_karyawan = input("Nama Karyawan           : ")
        golongan = int(input("Golongan Jabatan (1/2/3): "))
        pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
        jam_kerja = int(input("Jumlah Jam Kerja (per hari): "))
    except ValueError:
        print(f"[ERROR] Input Golongan dan Jam Kerja harus berupa angka.")
        sys.exit(1)
    tunjangan_jabatan = hitung_tunjangan_jabatan(golongan)
    tunjangan_pendidikan = hitung_tunjangan_pendidikan(pendidikan)
    honor_lembur = hitung_honor_lembur(jam_kerja)
    total_honor = tunjangan_jabatan + tunjangan_pendidikan + honor_lembur
    total_gaji_diterima = GAJI_POKOK + total_honor
    persen_jabatan_display = {1: "5%", 2: "10%", 3: "15%"}.get(golongan, "0%")
    print("\n" + "=" * 42)
    print("           RINCIAN HONOR YANG DITERIMA            ")
    print("=" * 42)
    
    print(f"Karyawan yang bernama: {nama_karyawan}")
    print("-" * 42)
    print(f"Gaji Pokok             : {format_rupiah(GAJI_POKOK):>15}")
    print(f"Tunjangan Jabatan ({persen_jabatan_display:<3}) : {format_rupiah(tunjangan_jabatan):>15}")
    print(f"Tunjangan Pendidikan   : {format_rupiah(tunjangan_pendidikan):>15}")
    print(f"Honor Lembur           : {format_rupiah(honor_lembur):>15}")
    print("-" * 42)
    print(f"TOTAL GAJI DITERIMA    : {format_rupiah(total_gaji_diterima):>15}")
    print("=" * 42)
if __name__ == "__main__":
    main()