def cek_kata_sandi(kata_sandi):
    if len(kata_sandi) < 8 or len(kata_sandi) > 32:
        return "Kata sandi harus terdiri dari 8 hingga 32 karakter"

    if kata_sandi[0].isdigit():
        return "Karakter awal tidak boleh angka"

    if not any(char.isdigit() for char in kata_sandi):
        return "Harus memiliki angka"

    if not any(char.islower() for char in kata_sandi) or not any(char.isupper() for char in kata_sandi):
        return "Harus memiliki huruf kapital dan huruf kecil"

    return "Kata sandi valid"


# Contoh pemanggilan fungsi
kata_sandi1 = "5andiwara"
kata_sandi2 = "sandiwar4"
kata_sandi3 = "Sandiwar4"

output1 = cek_kata_sandi(kata_sandi1)
output2 = cek_kata_sandi(kata_sandi2)
output3 = cek_kata_sandi(kata_sandi3)

print(output1)
print(output2)
print(output3)
