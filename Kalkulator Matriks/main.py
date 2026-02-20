                                                            # Python Library
from tkinter import *               # Mengimport semua modul yang ada pada tkinter 
from tkinter import messagebox,Label,Entry   # Mengimport messagebox yang ada pada tkinter
import numpy as np                  # Mengimport numpy dengan nama alias np
import time                         # Mengimport time

                                                            # GUI Layout  \                                                          # GUI Layout                                                           

root = Tk()                                                                 # Mengisi variabel root dengan TK() dari tkinter                
root.geometry("500x500")                                                    # Mengatur ukuran window GUI sebesar 500x500
root.title("Kalkulator Matriks")                        # Mengatur title GUI yang terletak dikanan icon
root.configure(bg = "#474E61")                                              # Memberi warna background GUI





tops = Frame(root, width=500, height=50, bg="#474E61")
tops.pack(side=TOP)


tops = Frame(root, width = 500, height = 50, bg = "#474E61")    # tops layout
tops.pack(side = TOP)                                           # Mengatur posisi tops layout

f1 = Frame(root, width = 500, height = 100, bg = "#474E61")     # f1 layout
f1.pack(side = TOP, pady = (16, 0))                             # Mengatur posisi tops layout

f2 = Frame(root, width = 500, height = 100, bg = "#474E61")     # f2 layout
f2.pack(side = TOP, pady = (32, 0))                             # Mengatur posisi tops layout

f3 = Frame(root, width = 500, height = 100, bg = "#474E61")     # f3 layout
f3.pack(side = TOP, pady = (32, 0))                             # Mengatur posisi tops layout

f4 = Frame(root, width = 500, height = 100, bg = "#474E61")     # f4 layout
f4.pack(side = TOP, pady = (32, 0))                             # Mengatur posisi tops layout




                                                            # Function
def Generate():
    # Handling Exceptions
    try:
        # Mengubah nilai state button                                      
        generate["state"] = DISABLED; 
        save["state"] = NORMAL    
        destroy["state"] = NORMAL

        # Mendeklarasikan variabel global dan mengambil nilai M dan N
        global M; global N; global rows1   
        M = int(eRA.get())                 
        N = int(eCA.get())            

        # Membuat judul matriks B dan mengatur posisinya    
        titleA = Label(f3, font = ("arial", "9", "bold"), text = "Matriks A", bg = "#474E64", fg = "#FFFFFF")  
        titleA.grid(row = 0, column = 0, columnspan = N)                                                      

        # Membuat entry untuk matriks A sesuai masukan dari pengguna
        rows1 = []                                                  
        for i in range(M):                                          
            cols1 = []                                              
            for j in range(N):                                      
                entry = Entry(f3, width= 5, justify = "center")     
                entry.grid(row = i+1, column = j)                   
                cols1.append(entry)                                 
            rows1.append(cols1)                                     

        # Mendeklarasikan variabel global dan mengambil nilai P dan Q
        global P; global Q; global rows2  
        P = int(eRB.get())                 
        Q = int(eCB.get())            

        # If statement
        if (P > 0) and (Q > 0):
            # Membuat judul matriks B dan mengatur posisinya                                                                           
            titleB = Label(f3, font = ("arial", "9", "bold"), text = "Matriks B", bg = "#474E64", fg = "#FFFFFF")  
            titleB.grid(row = 0, column = N, columnspan = Q, padx = (50, 0))                                       

            # Membuat entry untuk matriks B sesuai masukan dari pengguna  
            rows2 = []                                              
            for i in range(P):                                      
                cols2 = []                                          
                for j in range(Q):                                  
                    if (j == 0):                                    
                        pad = (50, 0)                               
                    else:                                          
                        pad = (0, 0)                               
                    entry = Entry(f3, width = 5, justify = "center")    
                    entry.grid(row = i+1, column = j+N, padx = pad)     
                    cols2.append(entry)                                
                rows2.append(cols2)                                     

        # Mendeklarasikan variabel global dan mengambil nilai K
        global K
        K = int(eNK.get())

    # Handling Exceptions
    except:                 
        # Mengubah nilai state button                                       
        generate["state"] = NORMAL; save["state"] = DISABLED   
        destroy["state"] = DISABLED

        # Menampilkan messagebox bila error
        messagebox.showinfo(title = "informasi", message = "Mohon isi data dengan benar") 

def Destroy():
    # Mengubah nilai state button  
    delete["state"] = DISABLED; add["state"] = DISABLED
    subtract["state"] = DISABLED; multiply["state"] = DISABLED
    destroy["state"] = DISABLED; scalar["state"] = DISABLED
    generate["state"] = NORMAL

    # Menghapus value dari widget entry(baris dan kolom) pada f1
    for widget in f1.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, "end")

    # Mengisi baris dan kolom dengan nilai default 0
    eRA.insert(0, 0); eCA.insert(0, 0); eRB.insert(0, 0); eCB.insert(0, 0); eNK.insert(0, 0)

    # Menghapus semua widget yang ada pada f3
    for widget in f3.winfo_children():
        widget.destroy()

    # Menghapus semua widget yang ada pada f4
    for widget in f4.winfo_children():
        widget.destroy()


def Save():
    # Handling Exceptions
    try:
        # Mendeklarasikan variabel global( A(Matriks A), B(Matriks B) )
        global A
        global B
        global K  # Mendeklarasikan K sebagai variabel global

        # Mengubah nilai state button
        save["state"] = DISABLED; 
        delete["state"] = NORMAL

        # If-elif-else statement 
        if (P > 0) and (Q > 0):                                            
            add["state"] = NORMAL
            subtract["state"] = NORMAL
            multiply["state"] = NORMAL
            scalar["state"] = NORMAL
            transpose["state"] = NORMAL
            determinant["state"] = NORMAL  
        elif (K > 0):                                                       
            scalar["state"] = NORMAL
            transpose["state"] = NORMAL
        else:                                                               
            scalar["state"] = DISABLED
            transpose["state"] = DISABLED
            determinant["state"] = DISABLED  

        # Membuat list dengan nama entriesA 
        entriesA = []

        # Mengambil nilai dari kolom entry, lalu ditambahkan ke dalam list entriesA
        for row in rows1:                           
            for col in row:                         
                entriesA.append(int(col.get()))
        
        # Mengubah list entriesA menjadi numpy array yang di reshape(M, N) --> A
        A = np.array(entriesA).reshape(M, N)

        # If statement
        if (P > 0) and (Q > 0):

            # Membuat list dengan nama entriesB --> matriks B
            entriesB = []           

            # Mengambil nilai dari kolom entry, lalu ditambahkan ke dalam list entriesB
            for row in rows2:                           
                for col in row:                         
                    entriesB.append(int(col.get()))     
            
            # Mengubah list entriesB menjadi numpy array yang di reshape(P, Q) --> B
            B = np.array(entriesB).reshape(P, Q)
        
        # Mengambil nilai skalar K
        K = int(eNK.get())
        
        # Aktifkan tombol-tombol yang relevan dengan kondisi yang ada setelah data disimpan
        if (P > 0) and (Q > 0):                                            
            add["state"] = NORMAL
            subtract["state"] = NORMAL
            multiply["state"] = NORMAL
        elif (K > 0):                                                       
            scalar["state"] = NORMAL

    # Handling Exceptions
    except:                                               
        # Mengubah nilai state button      
        save["state"] = NORMAL; delete["state"] = DISABLED
        add["state"] = DISABLED; subtract["state"] = DISABLED
        scalar["state"] = DISABLED
        transpose["state"] = DISABLED
        determinant["state"] = DISABLED  # Nonaktifkan tombol determinan
        
        # Menampilkan messagebox bila error
        messagebox.showinfo(title="informasi", message="Entri matriks masih kosong")



def Delete():
    # Mengubah nilai state button
    delete["state"] = DISABLED; add["state"] = DISABLED         
    subtract["state"] = DISABLED; multiply["state"] = DISABLED

    # Menghapus value dari widget entry pada f3
    for widget in f3.winfo_children():      
        if isinstance(widget, Entry):
            widget.delete(0, "end")         
    
    # Menghapus semua widget yang ada pada f4
    for widget in f4.winfo_children():      
        widget.destroy()                    

def Add():
    # Handling Exceptions
    try:  
        # Penjumlahan matriks A dan matriks B --> Matriks C                                 
        C = A + B   # Penjumlahan numpy array (Elementwise Operation)
    except: 
        # Menampilkan messagebox bila error(tidak dapat dijumlahkan)                                
        messagebox.showinfo(title = "syarat", message = "Ordo kedua matriks harus sama")    

    # Menghapus semua widget yang ada pada f4
    for widget in f4.winfo_children():      
        widget.destroy()                    

    # Membuat label(A + B) pada f4 dan mengatur posisinya
    titleC = Label(f4, font = ("arial", "9", "bold"), text = "A + B", bg = "#474E64", fg = "#FFFFFF")
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))                                           

    # Membuat, mengatur posisi, dan mengisi widget entry(Matriks C)
    for i in range(len(C)):                                     
        for j in range(len(C[0])):                              
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                   
            entry.insert(0, C[i, j])
            
            # Penjelasan cara perhitungan
        explanation = Label(f4, text="Cara Perhitungan:\n"
                                    "Untuk menghasilkan dari hasil penjumlahan A + B,\n"
                                    "kita cukup menjumlahkan dari matriks A dengan elemen pada baris dan kolom yang sama\n"
                                    "dari matriks B\n", 
                            font=("arial", "9"), bg="#474E64", fg="#FFFFFF")
        explanation.grid(row=len(C) + 1, column=0, columnspan=len(C[0]), padx=10, pady=(10, 0))
                                                    

def Subtract():
    # Handling Exceptions
    try:              
        # Pengurangan matriks A dan matriks B --> Matriks C                      
        C = A - B   # Pengurangan numpy array (Elementwise Operation)              
    except:                                 
        # Menampilkan messagebox bila error(tidak dapat dikurangi)
        messagebox.showinfo(title = "syarat", message = "Ordo kedua matriks harus sama")    

    # Menghapus semua widget yang ada pada f4
    for widget in f4.winfo_children():
        widget.destroy()                     

    # Membuat widget label(A - B) pada f4 dan mengatur posisinya
    titleC = Label(f4, font = ("arial", "9", "bold"), text = "A - B", bg = "#474E64", fg = "#FFFFFF") 
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))                                           

    # Membuat, mengatur posisi, dan mengisi widget entry(Matriks C)
    for i in range(len(C)):                                     
        for j in range(len(C[0])):                              
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                   
            entry.insert(0, C[i, j])    
            
            # Penjelasan cara perhitungan
        explanation = Label(f4, text="Cara Perhitungan:\n"
                                    "Untuk menghasilkan dari hasil pengurangan A - B,\n"
                                    "kita cukup mengurangkan dari matriks A dengan elemen pada baris dan kolom yang sama\n"
                                    "dari matriks B\n", 
                            font=("arial", "9"), bg="#474E64", fg="#FFFFFF")
        explanation.grid(row=len(C) + 1, column=0, columnspan=len(C[0]), padx=10, pady=(10, 0))
                        

def Multiply():
    # Handling Exceptions
    try:         
        # Perkalian matriks A dan matriks B --> Matriks C                           
        C = np.dot(A, B)    # Perkalian matriks menggunakan fungsi dari numpy                    
    except:                                
        # Menampilkan messagebox bila error(tidak dapat dikurangi)
        messagebox.showinfo(title = "syarat", message = "Jumlah kolom Matriks A sama dengan jumlah baris Matriks B\n"
        "atau Ordo kedua matriks harus sama")                                               

    # Menghapus semua widget yang ada pada f4
    for widget in f4.winfo_children():
        widget.destroy()                    

    # Membuat widget label(A x B) pada f4 pada f4 dan emngatur posisinya
    titleC = Label(f4, font = ("arial", "9", "bold"), text = "A x B", bg = "#474E64", fg = "#FFFFFF")  
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))                                           

    # Membuat, mengatur posisi, dan mengisi widget entry(Matriks C)
    for i in range(len(C)):                                     
        for j in range(len(C[0])):                             
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                  
            entry.insert(0, C[i, j])
        
        # Penjelasan cara perhitungan
        explanation = Label(f4, text="Cara Perhitungan:\n"
                                    "Untuk menghasilkan perkalian A x B,\n"
                                    "kita mengalikan setiap elemen pada baris dari matriks A\n"
                                    "dengan elemen pada kolom dari matriks B, lalu menjumlahkannya.", 
                            font=("arial", "9"), bg="#474E64", fg="#FFFFFF")
        explanation.grid(row=len(C) + 1, column=0, columnspan=len(C[0]), padx=10, pady=(10, 0))



def Determinant():
    try:
        # Menghitung determinan matriks A
        det_A = (np.linalg.det(A))
        
        # Menghitung determinan matriks B
        det_B =(np.linalg.det(B))
        
        # Menghapus semua widget yang ada pada f4
        for widget in f4.winfo_children():
            widget.destroy()
        
        # Menampilkan label dan nilai determinan matriks A di GUI
        titleDetA = Label(f4, font=("arial", "9", "bold"), text="Determinan(A)", bg="#474E64", fg="#FFFFFF")
        titleDetA.grid(row=0, column=0)
        
        # Menampilkan nilai determinan matriks A
        entryDetA = Entry(f4, width=10, justify="center")
        entryDetA.grid(row=0, column=1)
        entryDetA.insert(0, det_A)

        # Menampilkan label dan nilai determinan matriks B di GUI
        titleDetB = Label(f4, font=("arial", "9", "bold"), text="Determinan(B)", bg="#474E64", fg="#FFFFFF")
        titleDetB.grid(row=1, column=0)

        # Menampilkan nilai determinan matriks B
        entryDetB = Entry(f4, width=10, justify="center")
        entryDetB.grid(row=1, column=1)
        entryDetB.insert(0, det_B)
        
        # Menampilkan cara perhitungan determinan
        explanation = Label(f4, text="Cara Perhitungan:\n"
                                    "Untuk matriks A dan B, determinannya dihitung menggunakan fungsi np.linalg.det() dari NumPy.\n"
                                    "Metode yang digunakan bergantung pada ukuran matriks, namun secara umum, ekspansi kofaktor\n"
                                    "atau metode reduksi baris digunakan untuk menghitung determinannya.",
                        font=("arial", "9"), bg="#474E64", fg="#FFFFFF")
        explanation.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0))

    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi
        messagebox.showinfo(title="Error", message=str(e))



def Scalar():
    try:
        # Perkalian matriks A dan skalar K --> Matriks C
        C = A * K
        
        # Perkalian matriks B dan skalar K --> Matriks C_B
        C_B = B * K

        # Menghapus semua widget yang ada pada f4
        for widget in f4.winfo_children():
            widget.destroy()                    

        # Membuat dan mengatur posisi widget label(A x K) pada f4
        titleC = Label(f4, font=("arial", "9", "bold"), text="A x K", bg="#474E64", fg="#FFFFFF")  
        titleC.grid(row=0, column=0, columnspan=len(C[0]))                                           

        # Membuat dan mengatur posisi widget label(B x K) pada f4
        titleC_B = Label(f4, font=("arial", "9", "bold"), text="B x K", bg="#474E64", fg="#FFFFFF")
        titleC_B.grid(row=0, column=len(C[0]) + 1, columnspan=len(C_B[0]))

        # Membuat, mengatur posisi, dan mengisi widget entry untuk matriks C
        for i in range(len(C)):                                     
            for j in range(len(C[0])):                              
                entry = Entry(f4, width=5, justify="center")     
                entry.grid(row=i + 1, column=j)                   
                entry.insert(0, C[i, j])

        # Membuat, mengatur posisi, dan mengisi widget entry untuk matriks C_B
        for i in range(len(C_B)):
            for j in range(len(C_B[0])):
                entry = Entry(f4, width=5, justify="center")
                entry.grid(row=i + 1, column=len(C[0]) + j + 1)
                entry.insert(0, C_B[i, j])

        # Menampilkan cara perhitungan perkalian matriks A dengan skalar K
        calcA = Label(f4, font=("arial", "9", "bold"), text="Cara perhitungan A x K:", bg="#474E64", fg="#FFFFFF")
        calcA.grid(row=len(C) + 2, column=0, columnspan=len(C[0]), padx=(0, 20))
        
        detailA = "\n".join([f"Elemen A baris {i+1} kolom {j+1} dikalikan dengan K: {A[i][j]} * {K} = {C[i][j]}" for i in range(len(A)) for j in range(len(A[0]))])
        calc_detailA = Label(f4, font=("arial", "9"), text=detailA, bg="#474E64", fg="#FFFFFF", justify="left")
        calc_detailA.grid(row=len(C) + 3, column=0, columnspan=len(C[0]), padx=(0, 20))

        # Menampilkan cara perhitungan perkalian matriks B dengan skalar K
        calcB = Label(f4, font=("arial", "9", "bold"), text="Cara perhitungan B x K:", bg="#474E64", fg="#FFFFFF")
        calcB.grid(row=len(C) + 2, column=len(C[0]) + 1, columnspan=len(C_B[0]), padx=(20, 0))
        
        detailB = "\n".join([f"Elemen B baris {i+1} kolom {j+1} dikalikan dengan K = {B[i][j]} * {K} = {C_B[i][j]}" for i in range(len(B)) for j in range(len(B[0]))])
        calc_detailB = Label(f4, font=("arial", "9"), text=detailB, bg="#474E64", fg="#FFFFFF", justify="left")
        calc_detailB.grid(row=len(C) + 3, column=len(C[0]) + 1, columnspan=len(C_B[0]), padx=(20, 0))

    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi
        messagebox.showinfo(title="Error", message=str(e))

    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi
        messagebox.showinfo(title="Error", message=str(e))

def Transpose():
    try:
        # Menghitung transpose dari matriks A
        A_transpose = np.transpose(A)
        # Menghitung transpose dari matriks B
        B_transpose = np.transpose(B)
        
        # Menghapus semua widget yang ada pada frame f4
        for widget in f4.winfo_children():
            widget.destroy()
        
        # Menampilkan label dan nilai matriks transpose A di GUI
        titleA = Label(f4, font=("arial", "9", "bold"), text="A Transpose", bg="#474E64", fg="#FFFFFF")
        titleA.grid(row=0, column=0, columnspan=len(A_transpose[0]))

        # Menampilkan cara perhitungan transpose A
        calcA = Label(f4, font=("arial", "9", "bold"), text="Cara perhitungan A Transpose:", bg="#474E64", fg="#FFFFFF")
        calcA.grid(row=1, column=0, columnspan=len(A_transpose[0]))

        row_offset = 2  # Offset untuk baris data

        for i in range(len(A_transpose)):
            for j in range(len(A_transpose[0])):
                entry = Entry(f4, width=5, justify="center")
                entry.grid(row=i + row_offset, column=j)
                entry.insert(0, A_transpose[i, j])

        # Menampilkan label dan nilai matriks transpose B di GUI
        titleB = Label(f4, font=("arial", "9", "bold"), text="B Transpose", bg="#474E64", fg="#FFFFFF")
        titleB.grid(row=0, column=len(A_transpose[0]), columnspan=len(B_transpose[0]))

        # Menampilkan cara perhitungan transpose B
        calcB = Label(f4, font=("arial", "9", "bold"), text="Cara perhitungan B Transpose:", bg="#474E64", fg="#FFFFFF")
        calcB.grid(row=1, column=len(A_transpose[0]), columnspan=len(B_transpose[0]))

        for i in range(len(B_transpose)):
            for j in range(len(B_transpose[0])):
                entry = Entry(f4, width=5, justify="center")
                entry.grid(row=i + row_offset, column=len(A_transpose[0]) + j)
                entry.insert(0, B_transpose[i, j])

        # Menampilkan perhitungan detail transpose A
        row_calcA = row_offset + len(A_transpose) + 1
        detailA = "Transpose A:\n" + "\n".join([f"Baris {i+1} dari A menjadi Kolom {i+1} dari A Transpose" for i in range(len(A))])
        calc_detailA = Label(f4, font=("arial", "9"), text=detailA, bg="#474E64", fg="#FFFFFF", justify="left")
        calc_detailA.grid(row=row_calcA, column=0, columnspan=len(A_transpose[0]))

        # Menampilkan perhitungan detail transpose B
        row_calcB = row_offset + len(B_transpose) + 1
        detailB = "Transpose B:\n" + "\n".join([f"Baris {i+1} dari B menjadi Kolom {i+1} dari B Transpose" for i in range(len(B))])
        calc_detailB = Label(f4, font=("arial", "9"), text=detailB, bg="#474E64", fg="#FFFFFF", justify="left")
        calc_detailB.grid(row=row_calcB, column=len(A_transpose[0]), columnspan=len(B_transpose[0]))

    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi
        messagebox.showinfo(title="Error", message=str(e))


                                                            # GUI Layout (Tops)
localtime = time.asctime(time.localtime(time.time()))   # Fungsi mengambil waktu lokal

title = Label(tops, font = ("arial", "12", "bold"), text = "Demo Operasi Matriks", bg = "#474E64", fg = "#FFFFFF")
title.grid(row = 0, column = 0, pady = (8, 0)) # Judul program

date = Label(tops, text = localtime, bg = "#474E64", fg = "#FFFFFF")
date.grid(row = 1, column = 0, pady = (0, 8)) # Waktu lokal saat buka program

                                                            # GUI Layout (Frame 1 / f1)
# Label matriks A
mA = Label(f1, font=("arial", "9", "bold"), text="Matriks A", bg="#474E64", fg="#FFFFFF")
mA.grid(row=0, column=0, columnspan=2, pady=4)

# Label matriks B
mB = Label(f1, font=("arial", "9", "bold"), text="Matriks B", bg="#474E64", fg="#FFFFFF")
mB.grid(row=0, column=2, columnspan=2, padx=40, pady=4)

# Label skalar K
sK = Label(f1, font=("arial", "9", "bold"), text="Skalar K", bg="#474E64", fg="#FFFFFF")
sK.grid(row=0, column=4, columnspan=2, padx=40, pady=4)

# label baris (matriks A)
rA = Label(f1, text="Baris", bg="#474E64", fg="#FFFFFF")
rA.grid(row=1, column=0)
# Entry baris (matriks A)
eRA = Entry(f1, width=5, justify="center", relief=SUNKEN, bd=3)
eRA.grid(row=1, column=1)

# label baris (matriks B)
rB = Label(f1, text="Baris", bg="#474E64", fg="#FFFFFF")
rB.grid(row=1, column=2, padx=40)
# Entry baris (matriks B)
eRB = Entry(f1, width=5, justify="center", relief=SUNKEN, bd=3)
eRB.grid(row=1, column=3)

# Label Nilai (Skalar K)
nK = Label(f1, text="Nilai", bg="#474E64", fg="#FFFFFF")
nK.grid(row=1, column=4, padx=40)
# Entry Nilai (Skalar K)
eNK = Entry(f1, width=5, justify="center", relief=SUNKEN, bd=3)
eNK.grid(row=1, column=5)

# label kolom (matriks A)
cA = Label(f1, text="Kolom", bg="#474E64", fg="#FFFFFF")
cA.grid(row=2, column=0)
# Entry kolom (matriks A)
eCA = Entry(f1, width=5, justify="center", relief=SUNKEN, bd=3)
eCA.grid(row=2, column=1)

# label kolom (matriks B)
cB = Label(f1, text="Kolom", bg="#474E64", fg="#FFFFFF")
cB.grid(row=2, column=2, padx=40)
# Entry kolom (matriks B)
eCB = Entry(f1, width=5, justify="center", relief=SUNKEN, bd=3)
eCB.grid(row=2, column=3)

# Button generate
generate = Button(f1, text="Generate", command=Generate, width=8, relief=GROOVE, bg="#3C4559", fg="#FFFFFF")
generate.grid(row=1, column=6, padx=40)

# Button save
destroy = Button(f1, text="Destroy", command=Destroy, width=8, relief=GROOVE, bg="#FF5264", fg="#FFFFFF", state=DISABLED)
destroy.grid(row=2, column=6, padx=40, pady=(4, 0))

# Mengisi baris dan kolom matriks A dan B dengan nilai 0
eRA.insert(0, 0); eCA.insert(0, 0); eRB.insert(0, 0); eCB.insert(0, 0); eNK.insert(0, 0)

                                                            # GUI Layout (Frame 2 / f2)
# Button save --> Save
save = Button(f2, text="Save", width=12, height=1, command=Save, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
save.grid(row=0, column=1, padx=(0, 10), pady=(0, 4))

# Button delete --> Delete
delete = Button(f2, text="Delete", width=12, command=Delete, relief=GROOVE, bg="#FF5264", fg="#FFFFFF", state=DISABLED)
delete.grid(row=0, column=2, padx=(0, 10), pady=(0, 4))

# Button add --> Penjumlahan
add = Button(f2, text="Penjumlahan", width=12, command=Add, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
add.grid(row=0, column=3, padx=(0, 10), pady=(0, 4))

# Button subtract --> Pengurangan
subtract = Button(f2, text="Pengurangan", width=12, command=Subtract, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
subtract.grid(row=0, column=4, padx=(0, 10), pady=(0, 4))

# Button multiply --> Perkalian (Matriks)
multiply = Button(f2, text="Perkalian", width=12, command=Multiply, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
multiply.grid(row=0, column=5, padx=(0, 10), pady=(0, 4))

# Button scalar --> Perkalian skalar
scalar = Button(f2, text="Perkalian Skalar", width=12, command=Scalar, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
scalar.grid(row=1, column=2, padx=(0, 10), pady=(0, 4))  # Kolom diganti menjadi 3

# Button transpose --> Transpose
transpose = Button(f2, text="Transpose", width=12, command=Transpose, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
transpose.grid(row=1, column=4, padx=(0, 10), pady=(0, 4))  # Kolom diganti menjadi 5

#tombol untuk menghitung determinan
determinant = Button(f2, text="Determinan", width=12, command=Determinant, relief=GROOVE, bg="#3C4559", fg="#FFFFFF", state=DISABLED)
determinant.grid(row=1, column=3, padx=(0, 10), pady=(0, 4))


                                                            # Mainloop Window Tkinter

root.mainloop()
