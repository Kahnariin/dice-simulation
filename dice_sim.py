import random

#öncelikle terminalde çizdirilecek zarların ASCII kodlarını yazarak terminalden kopyalanılır.
#print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘


# Kopyalanilan karakterleri kullanarak bir sembol sözlüğü oluşturuluyor.
zarsembolleri = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

#sözlükteki her anahtar zar numarasını veriyor. Böylece .get metodu ile matematiksel fonksiyonların sonucuna bağlı olarak istenilen karakteri yazdırabilecektir.
zarlar = [] #boş bir liste tanımlanıyor.
toplam = 0  #zar toplamlarını vermesi için bir değişken tanımlanıyor.
zarmiktari = int(input("Zar adedini giriniz: ")) #kullanıcıdan kullanılacak zar miktarı isteniyor.

#Bu döngüde kullanıcıdan alınan girdiye göre zar miktarları belirlenip rastgele zar yuvarlanıyor.
for zar in range(zarmiktari):
    zarlar.append(random.randint(1,6))

#Bu döngüde zar sembollerinin ekrana yazdırılabilmesi için string manipülasyonu kullanılıyor. Aşağıdaki döngü zarların yan yana gösterilmesini sağlamak için tasarlanmış olup, dikey gösterime nispeten daha karmaşıktır.
for satir in range(5):
    for zar in zarlar:
        print(zarsembolleri.get(zar)[satir], end="") #zar sembolleri birer string olduğundan yazdırılırken beyaz boşluklardan meydana gelen kaymayı önlemek için her satır sonuna bir adet boş string yazdırılıyor. 
    print() #iç döngüde düzenlenen semboller satır bazında yazdırılıyor.

#Bu döngüde zarların toplamı hesaplanır.
for zar in zarlar:
    toplam += zar
print(f"toplam: {toplam}")
