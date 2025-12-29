class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savatcha:
    def __init__(self):
        self.mahsulotlar = []

    def qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
        print(f"✅ {mahsulot.nom} savatchaga qo‘shildi")

    def chiqarish(self):
        if not self.mahsulotlar:
            print("🛒 Savatcha bo‘sh")
        else:
            print("🛍 Savatchadagi mahsulotlar:")
            jami = 0
            for m in self.mahsulotlar:
                print(f"- {m.nom}: {m.narx} so‘m")
                jami += m.narx
            print(f"💰 Jami summa: {jami} so‘m")


savatcha = Savatcha()

olma = Mahsulot("Olma", 5000)
non = Mahsulot("Non", 3000)
sut = Mahsulot("Sut", 7000)

savatcha.qoshish(olma)
savatcha.qoshish(non)
savatcha.qoshish(sut)

print()
savatcha.chiqarish()
