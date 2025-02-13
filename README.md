GÜZERGAH PLANLAMASI

Proje Amacı
Projenin temel amacı, belirli kriterler (nüfus yoğunluğu, ulaşım altyapısı, maliyet analizi, çevresel etki, sosyal fayda) üzerinden mahalleleri değerlendirmek ve bu değerlendirmeye göre en uygun güzergahı belirlemektir. Ayrıca, maliyet-fayda analizi yaparak mahallelerin verimliliğini ölçer.

Kullanılan Teknolojiler
Python: Projenin temel programlama dili.

Matematiksel Hesaplamalar: Softmax normalizasyonu, ağırlıklı ortalama ve maliyet-fayda oranı hesaplamaları.

Softmax Algoritması Nedir?
Softmax, makine öğrenimi ve istatistikte sıkça kullanılan bir normalizasyon fonksiyonudur. Bir dizi gerçek sayı alarak, bunları 0 ile 1 arasında değerlere dönüştürür ve toplamlarının 1 olmasını sağlar. Bu, özellikle olasılık dağılımları oluşturmak için kullanılır.

Nasıl Çalışır?
Kriterler ve Ağırlıklar:
Her mahalle, belirli kriterlere göre değerlendirilir.
Kriterlerin ağırlıkları, Softmax fonksiyonu kullanılarak normalize edilir.

Mahalle Puanlaması:
Her mahalle için kriterlerin ağırlıklı toplamı hesaplanır.
Bu puanlar, mahallelerin performansını sayısal olarak ifade eder.

Güzergah Belirleme:
Mahalleler, toplam puanlarına göre yüksekten düşüğe doğru sıralanır.
En yüksek puana sahip mahalle, güzergahın başlangıç noktası olarak belirlenir.

Maliyet-Fayda Analizi:

Her mahalle için maliyet ve fayda değerleri hesaplanır.
Maliyet-fayda oranı, mahallelerin verimliliğini gösterir.
Düşük maliyet-fayda oranı, daha iyi bir performansı ifade eder.

Kod Yapısı
softmax(x): Kriter ağırlıklarını normalize eder.

toplam_puanlar: Her mahalle için ağırlıklı toplam puanları hesaplar.

mahalle_puan_eslesmesi: Mahalleleri puanlarına göre sıralar.

maliyet_fayda_oranlari: Her mahalle için maliyet-fayda oranını hesaplar.

Nasıl Kullanılır?
Kodu Çalıştırma:

Proje dosyasını indirin ve Python ortamında çalıştırın.
Örnek çıktılar terminalde görüntülenecektir.

Çıktılar:

Kriter Ağırlıkları (Softmax): Normalize edilmiş kriter ağırlıkları.

Mahallelerin Toplam Puanları: Her mahallenin performans puanı.

Önerilen Güzergah Sıralaması: En uygun güzergah sıralaması.

Maliyet-Fayda Analizi: Her mahalle için maliyet-fayda oranı.

Örnek Çıktı

Kriter Ağırlıkları (Softmax): [0.4582911088913556, 0.16859587703279252, 0.16859587703279252, 0.10225856852152966, 0.10225856852152966]
Mahallelerin Toplam Puanları: [4.2349331855440555, 3.9982396874017847, 6.833164435565422]
Önerilen Güzergah Sıralaması: İstasyon Mahallesi -> Karakaş Mahallesi -> Karahıdır Mahallesi

Maliyet-Fayda Analizi:
İstasyon Mahallesi: Maliyet-Fayda Oranı = 0.27
Karakaş Mahallesi: Maliyet-Fayda Oranı = 0.49
Karahıdır Mahallesi: Maliyet-Fayda Oranı = 0.84
