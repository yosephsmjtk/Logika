def tampilkan_kelipatan(N):
    output = []
    i = 1
    while len(output) < N:
        if i % 3 == 0 and i % 7 == 0:
            output.append("Z")
        elif i % 3 == 0 or i % 7 == 0:
            output.append(i)
        i += 1

    print(", ".join(str(x) for x in output[:N]))


# Contoh pemanggilan fungsi
N = 22
tampilkan_kelipatan(N)
