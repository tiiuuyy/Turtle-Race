# from codecs import namereplace_errorsJarak_Turtle
import turtle # Digunakan agar kita bisa menggunakan turtle 
import time #digunakan untuk meng-import modul time 
import random #digunakan untuk mengacak nilai dalam variabel
import os #memanggil modul operating system
import threading
from tkinter import * #Tkinter merupakan pustaka standar yang digunakan untuk membuat aplikasi berbasis GUI pada bahasa pemrograman python
from tkinter import messagebox
import tkinter as tk

Jarak_Turtle = 700 #jarak t1 dan t2 sumbu x
Posisi_Start = 580 #y 

window = tk.Tk()
window.title("TURTLE RACE!!")
cnv = tk.Canvas(window, width=1000, height=700) #Untuk menentukan ukuran tampilan window
cnv.pack() #Fungsi yang sering digunakan dalam mengatur widget

countdown = 3
final_winner =''

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan'] #Menampilkan pilihan warna yang nantinya akan dipilih

def clearscreen(): #fungsi untuk membersihkan terminal
    os.system('cls' if os.name == 'nt' else 'clear') #untuk membersihkan terminal dengan memanggil modul operating system 

def startThread():
    #Thread
    thrdStartRace = threading.Thread(target=startRace, args=())
    thrdHitungMundur = threading.Thread(target=HitungMundur(countdown), args=())
    
    thrdHitungMundur.start()
    thrdStartRace.start()    
    buttonRace.config(state = DISABLED)
    
def HitungMundur(count):
    # change text in label        
    labelHitungMundur['text'] = count

    if count > 0:
        cnv.after(1000, HitungMundur, count-1)
        
def validasiInputAngka_countdown():
    try:
        tempInput = int(inputTotalPemain.get())
        if tempInput in range(2,10):
            labelTextPermainan.config(text='Permainan akan dimulai : ')
            startThread()
        else:
            messagebox.showinfo("Error", "Masukan antara 2 - 10")
    except ValueError:
        messagebox.showinfo("Error", "Masukan hanya Bilangan Bulat")

def startRace():
    global countdown
    while countdown > 0:
        time.sleep(1)
        countdown -=1
        if countdown == 0:
            mainProgram()
        
def mainProgram():
    global final_winner
    racers = int(inputTotalPemain.get()) #digunakan untuk mendapatkan jumlah pemain turtle yang diinginkan user 
    init_turtle() #digunakan untuk memanggil fungsi init turtle 

    random.shuffle(COLORS) #digunakan untuk mengubah urutan warna yang ada pada list 
    colors = COLORS[:racers] #digunakan untuk mendapatkan substring warna racers 

    winner = race(colors) #digunakan untuk mengatur warna pemenang turtle
    final_winner = str(winner) 
    labelTextPemenang.config(text='Pemenangnya adalah     : ')
    labelPemenang.config(text=str(winner))
    time.sleep(2) #digunakan untuk memberikan jeda waktu selama 2 detik
    
    closing() #digunakan untuk memanggil fungsi closing 
      
labelHitungMundur = Label(cnv,fg='black', font=('Arial',12))
labelHitungMundur.grid(row=5, column=1,padx=5,pady=10)

dataNama = StringVar()
dataPemain = IntVar()

#Label nama
labelNama = Label(cnv, text='Masukkan nama Anda     : ',fg='black', font=('Arial',12))
labelNama.grid(row=0, column=0,padx=5,pady=10)

#Text input nama
inputNama = Entry(cnv, textvariable= dataNama ,fg='black', font=('Arial',12))
inputNama.grid(row=0, column=1,padx=5)

#Label jumblah pemain
labelTotalPemain = Label(cnv, text='Masukkan Total Pemain  : ',fg='black', font=('Arial',12))
labelTotalPemain.grid(row=1, column=0,padx=5,pady=8)

#Input Jumlah Pemain
inputTotalPemain = Entry(cnv, textvariable= dataPemain,fg='black', font=('Arial',12))
inputTotalPemain.grid(row=1, column=1,padx=5)

#Label ket input player 2-10
ket = Label(cnv, text='2-10',fg='black', font=('Arial',12))
ket.grid(row=1, column=2,padx=5,pady=10)

#tombol
buttonRace = Button(cnv, command = validasiInputAngka_countdown, text='RACE', fg='black', font=('Arial',12), width=20)
buttonRace.grid(row=2, column=1,sticky=W)

#Label text permainan
labelTextPermainan = Label(cnv,fg='black', font=('Arial',12))
labelTextPermainan.grid(row=5, column=0,padx=5,pady=10)

#Label Textplayer menang
labelTextPemenang = Label(cnv, fg='black', font=('Arial',12))
labelTextPemenang.grid(row=6, column=0,padx=5,pady=10)

#Label Textplayer menang
labelPemenang = Label(cnv, fg='black', font=('Arial',12))
labelPemenang.grid(row=6, column=1,padx=5,pady=10)

def race(colors): #fungsi untuk mengatur warna lintasan turtle 
	turtles = create_turtles(colors) #digunakan untuk membuat warna pada turtle 

	while True: #perulangan untuk mengacak turtle 
		for racer in turtles: #perulangan untuk turtle racer 
			distance = random.randrange(1, 20) #digunakan untuk memilih secara acak elemen pada rentang yang telah ditentukan 
			racer.forward(distance) #digunakan untuk menggerakkan turtle maju sejauh jarak yang telah ditentukan

			x, y = racer.pos() #digunakan untuk mengatur posisi turtle 
			if y >= Posisi_Start // 2 - 10: #digunakan untuk mengatur range ketinggian sesuai dengan jumlah turtle yang telah ditentukan sebelumnya 
				return colors[turtles.index(racer)] #digunakan untuk mengembalikan nilai yang tersimpan dalam variabel colors dengan indeks jumlah racer 

def create_turtles(colors): #fungsi untuk mengatur warna turtle 
	turtles = [] #list kosong untuk menampung nilai 
	spacingx = Jarak_Turtle // (len(colors) + 1) #digunakan untuk mengatur jarak x 
	for i, color in enumerate(colors): #digunakan untuk menampilkan turtle yang telah terdapat warnanya 
		racer = turtle.Turtle() #digunakan untuk menampilkan turtle di canvas 
		racer.color(color) #digunakan untuk mengatur warna turtle 
		racer.shape('turtle') #digunakan untuk mengatur bentuk objek yaitu turtle
		racer.left(90) #digunakan untuk berputae 90 derajat ke arah kiri
		racer.penup() #digunakan untuk menaikkan head jika tidak ingin ada tinta walau dipindahkan
		racer.setpos(-Jarak_Turtle//2 + (i + 1) * spacingx, -Posisi_Start//2 + 20) #digunakan untuk mengatur jarak antara ujung canvas dengan turtle 
		racer.pendown() #digunakan untuk menurunkan head untuk menuliskan tinta 
		turtles.append(racer) #digunakan untuk menambahkan turtle ke racer 

	return turtles #digunakan untuk mengembalikan nilai yang tersimpan di dalam variabel turtles kepada kode yang akan memanggil fungsi tersebut

def init_turtle(): #fungsi untuk mengatur window turtle race 
    screen = turtle.Screen() #digunakan untuk membuat objek window
    screen.bgcolor("lightgreen") #digunakan untuk memberi warna backgorund di window 
    # screen.setup(Jarak_Turtle, Posisi_Start) #digunakan untuk mengatur ukuran window 
    screen.title('Turtle Racing! - Player : ' + str(dataNama.get())) #digunakan untuk memberi judul paada window 
 
def closing():#fungsi untuk menampilkan closing kepada user 
    messagebox.showinfo('Akhir game','Terima kasih ' + str(dataNama.get()) + ' sudah memainkan game ini. Pemenangnya adalah : ' + final_winner)
    os._exit(0)
        
cnv.mainloop()