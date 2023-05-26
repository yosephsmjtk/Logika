def cari_kata(teks):
    kata_kunci = ["sang gajah", "serigala", "harimau"]
    hasil = []
    teks = teks.lower()  # Mengubah seluruh teks menjadi huruf kecil

    for kata in kata_kunci:
        count = teks.count(kata)
        hasil.extend([kata] * count)
        kata = kata.lower()  # Mengubah kata kunci menjadi huruf kecil

    return " - ".join(hasil)


# Contoh pemanggilan fungsi
teks = "Berikut adalah kisah sang gajah. Sang gajah memiliki  sang gajah teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah."
output = cari_kata(teks)
print(output)
