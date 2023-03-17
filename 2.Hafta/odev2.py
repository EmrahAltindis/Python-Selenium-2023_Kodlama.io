ogrenciler = []

def ogrenci_ekle(*args):
    for ogrenci in args:
        ogrenciler.append(ogrenci)
        print(f"{ogrenci} eklendi.")

def ogrenci_sil(ad, soyad):
    for ogrenci in ogrenciler:
        if ogrenci[0] == ad and ogrenci[1] == soyad:
            ogrenciler.remove(ogrenci)
            print(f"{ogrenci} silindi.")

def ogrencileri_listele():
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenci_numarasi(ad, soyad):
    for i, ogrenci in enumerate(ogrenciler):
        if ogrenci[0] == ad and ogrenci[1] == soyad:
            print(f"{ad} {soyad} öğrencisi {i} numaralı öğrencidir.")

def ogrencileri_coklu_sil(*args):
    while args:
        ad, soyad = args[:2]
        args = args[2:]
        ogrenci_sil(ad, soyad)

ogrenci_ekle(("Emrah", "Altındiş"), ("Zehra", "Altındiş"), ("Sevil", "Topal"))
ogrencileri_listele()
ogrenci_sil("Sevil", "Topal")
ogrencileri_listele()
ogrenci_numarasi("Emrah", "Altındiş")
ogrencileri_coklu_sil("Ahmet", "Altındiş", "Emrah", "Hüseyin")
ogrencileri_listele()