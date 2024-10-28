x = [5, 5, 10, 3, 2, 6, 7]
y1 = int(input("Masukkan angka yang ingin dicari (y1): "))
y2 = int(input("Masukkan angka yang ingin dicari (y2): "))

boolean_y1 = False
boolean_y2 = False

for i in range(len(x)):
    if x[i] == y1:
        print(f"Element {y1} didapatkan pada indeks ke {i}")
        found_y1 = True
    if x[i] == y2:
        print(f"Element {y2} didapatkan pada indeks ke {i}")
        found_y2 = True

if not found_y1:
    print(f"Element {y1} tidak ditemukan, ")
    print(0)
if not found_y2:
    print(f"Element {y2} tidak ditemukan,")
    print(0)
