import math

# Mahalle ve kriter bilgileri
mahalleler = ["Karakaş Mahallesi", "Karahıdır Mahallesi", "İstasyon Mahallesi"]
kriterler = ["Nüfus Yoğunluğu", "Mevcut Ulaşım Altyapısı", "Maliyet Analizi", "Çevresel Etki", "Sosyal Fayda"]

# Mahallelerin kriter değerleri
veriler = [
    [4, 3, 7, 2, 5],  # Karakaş Mahallesi
    [2, 5, 6, 8, 4],  # Karahıdır Mahallesi
    [9, 2, 8, 1, 9],  # İstasyon Mahallesi
]

# Kriter ağırlıkları
agirliklar = [3, 2, 2, 1.5, 1.5]

# Softmax fonksiyonu
def softmax(x):
    exp_x = [math.exp(i - max(x)) for i in x]
    sum_exp_x = sum(exp_x)
    return [i / sum_exp_x for i in exp_x]

normalize_edilmis_agirliklar = softmax(agirliklar)

#Her mahalle için kriterlerin ağırlıklı toplamını hesaplayarak, mahallelerin performansını sayısal bir değerle ifade eder.
toplam_puanlar = []
for mahalle in veriler:
    toplam = sum(mahalle[i] * normalize_edilmis_agirliklar[i] for i in range(len(kriterler)))
    toplam_puanlar.append(toplam)

# (mahalleler) ile hesaplanan (toplam_puanları) eşleştirir ve bu eşleşmeyi puanlara göre yüksekten düşüğe doğru sıralar.
mahalle_puan_eslesmesi = list(zip(mahalleler, toplam_puanlar))
mahalle_puan_eslesmesi.sort(key=lambda x: x[1], reverse=True)

# Sıraladığım mahalleler ile bir güzergah belirler.
guzergah = [mahalle for mahalle, _ in mahalle_puan_eslesmesi]

# Maliyet-Fayda Analizi
# Maliyet kriterleri: Maliyet Analizi (index 2), Çevresel Etki (index 3)
# Fayda kriterleri: Nüfus Yoğunluğu (index 0), Mevcut Ulaşım Altyapısı (index 1), Sosyal Fayda (index 4)

maliyet_index = [2, 3]
fayda_index = [0, 1, 4]

#Her bir maliyet kriterinin mahalledeki değeri ile o kriterin normalleştirilmiş ağırlığını çarparak ağırlıklı toplam hesaplıyor.
maliyet_fayda_oranlari = []
for i, mahalle in enumerate(veriler):
    maliyet = sum(mahalle[j] * normalize_edilmis_agirliklar[j] for j in maliyet_index)
    fayda = sum(mahalle[j] * normalize_edilmis_agirliklar[j] for j in fayda_index)
    maliyet_fayda_orani = maliyet / fayda if fayda != 0 else float('inf')  # Fayda 0 ise sonsuz olarak kabul et
    maliyet_fayda_oranlari.append((mahalleler[i], maliyet_fayda_orani))

# Maliyet-fayda oranlarına göre sıralar.
maliyet_fayda_oranlari.sort(key=lambda x: x[1])  # Düşük maliyet-fayda oranı en iyisidir


print("Kriter Ağırlıkları (Softmax):", normalize_edilmis_agirliklar)
print("Mahallelerin Toplam Puanları:", toplam_puanlar)
print("Önerilen Güzergah Sıralaması:", " -> ".join(guzergah))
print("\nMaliyet-Fayda Analizi:")
for mahalle, oran in maliyet_fayda_oranlari:
    print(f"{mahalle}: Maliyet-Fayda Oranı = {oran:.2f}")