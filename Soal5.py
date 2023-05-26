def create_pattern(N):
    if N % 2 == 0:  # Periksa apakah N adalah bilangan genap
        return "Harus bilangan ganjil"

    pattern = [['X'] * N for _ in range(N)]  # Membuat pola awal dengan semua elemen 'X'

    for i in range(1, N // 2 + 1):
        for j in range(i, N - i):
            pattern[i][j] = 'O'  # Mengubah elemen menjadi 'O' di dalam pola

    for row in pattern:
        print(''.join(row))  # Menampilkan pola baris per baris

# Contoh penggunaan:
N = int(input("Masukkan nilai N: "))
result = create_pattern(N)
if result:
    print(result)
