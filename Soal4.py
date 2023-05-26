def cari_bilangan_cacah_terkecil(data):
    data.sort()  # Mengurutkan urutan data
    
    smallest_missing = data[0] + 1  # Inisialisasi bilangan cacah terkecil yang hilang
    
    for num in data:
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            return smallest_missing
    
    return smallest_missing

# Contoh penggunaan
input1 = [5, 2, 8, 4, 3, 10]
output1 = cari_bilangan_cacah_terkecil(input1)
print("Output 1:", output1)  # Output: 6

input2 = [2, 3, 4, 6]
output2 = cari_bilangan_cacah_terkecil(input2)
print("Output 2:", output2)  # Output: 5

input3 = [8, 6, 7, 12]
output3 = cari_bilangan_cacah_terkecil(input3)
print("Output 3:", output3)  # Output: 9
