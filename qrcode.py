#tkinter'daki her şeyi dahil et ve ben tkinter'ı çağırmak istediğimde tk olarak getir. yani tkinter modülün tam adı ve resmi Python modülüdür.
#tk, genellikle daha kısa ve okunabilir olması için tercih edilen bir takma addır.
import tkinter as tk  
from tkinter import filedialog  #tkinterdan filedialogu ekle.
import pyqrcode                 #yazdığımızı qr'a çeviren modüldür. Biz yükledik yüklü değildi. 'pip install qrcode'
from pyqrcode import QRCode     #qr kodları oluşturucak objeyi çağırır.

def qr_kod():
    url= url_girdi.get()   #url'e girilen veriyi getirtmek için get kullanırız. 
    
#filedialog.asksaveasfile: Bu fonksiyon, bir "Dosya Kaydet" penceresi açar ve kullanıcıya bir dosya adı seçme veya yazma imkanı tanır.
#Amaç: Kullanıcıdan bir dosya adı ve konumu almak ve bu dosyayla işlem yapmak.
#Kullanıcı bir dosya adı yazdığında, eğer uzantı belirtmezse bu uzantı otomatik olarak eklenir.
#Örneğin, kullanıcı "deneme" yazarsa, dosya adı "deneme.svg" olarak tamamlanır.Eğer kullanıcı başka bir uzantı yazarsa, bu parametre etkisiz olur (örneğin, "deneme.txt" yazarsa uzantı değiştirilmez).
#[("SVG Dosyaları", "*svg")] şu anlama gelir:
#"SVG Dosyaları": Kullanıcıya gösterilecek açıklama.
#"*svg": Filtreleme deseni. Sadece .svg uzantılı dosyaları görüntüler.
#asksaveasfile, kullanıcının seçtiği dosya yolunu ve dosya nesnesini döner. Kullanıcı bir dosya seçmezse, None döner. Eğer kullanıcı dosya seçer veya oluşturursa, bu dosya nesnesi üzerinden yazma işlemleri yapılabilir.


    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG Dosyaları","*svg")])  

        if dosya_yolu:
            qr_url.svg(dosya_yolu,scale=8) #qr_url'i svg'ye çeviririz. Sonra da dosya yoluna kaydederiz. scale boyutunu temsil eder.
            durum_etiketi.config(text="QR KODU OLUŞTURULDU")



app_window = tk.Tk()
app_window.title("QR KOD")

etiket = tk.Label(app_window,text="URL GİRİNİZ: ")   #app_window'a ekler etiketi. 
url_girdi = tk.Entry(app_window,width=40)   #entry : kullanıcı bir şeyler girer. width genişlik.
qr_kod_buton = tk.Button(app_window,text="QR KOD OLUŞTUR",command=qr_kod)  #command = butona basıldığı zaman qr_kod fonk çalıştır.
durum_etiketi = tk.Label(app_window,text="") #boş bırakıyoruz çünkü eğer dosya kaydedildiyse yukardaki yazı yazılsın yazılmazsa boş dursun diye bi şey yazmayız.

# etiket.pack()
# url_girdi.pack()
# qr_kod_buton.pack()
# durum_etiketi.pack()

etiket.grid(row=0,column=0,padx=10,pady=10) 
url_girdi.grid(row=0,column=1,padx=10,pady=10) 
qr_kod_buton.grid(row=1,column=0,columnspan=2,padx=10,pady=10) 
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)  #columnspan=2   2 birimlik yer kapla demek.
app_window.resizable(0,0)

app_window.mainloop()