# Abi Rahmawan
# V3921001
# TI-D 

key=input("MASUKKAN KUNCI : ") # memassukkan kunci
print("================================")
key=key.replace(" ", "") # menghilangkan spasi
key=key.upper() # merubah ke dalam huruf kapital

# membuat fungsi matrix
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: # menyimpan kunci
    if c not in result:
        if c=='J': # mengecualikan huruf J
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): # menyimpan karakter lain
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) # inisialisasi matriks
for i in range(0,5): # membuat matriks
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

#  membuat fungsi untuk mendapatkan lokasi setiap karakter
def locindex(c): 
    loc=list()
    if c=='J': # mengecualikan huruf J
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

# Enkripsi   
def enkripsi():  
    msg=str(input("MASUKKAN KATA: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:] # menambah huruf X apabila jumlah huruf ganjil
    if len(msg)%2!=0:
        msg=msg[:]+'X' # menambah huruf X apabila jumlah huruf ganjil
    print("CIPHER TEXT: ",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        


# Deskripsi     
def deskripsi():  
    msg=str(input("MASUKKAN CIPHER TEXT: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT: ",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2      

# Pembuatan menu
print("==== METODE PLAYFAIR CHIPPER====")
print("1. Enkripsi")
print("2. Deskripsi")
print("3. Keluar")
print("================================")
menu = input("Pilih menu : ")
print("================================")


if menu == "1":
    enkripsi() # memanggil fungsi enkripsi
elif menu == "2":
    deskripsi() # memanggil fungsi deskripsi
elif menu == "3":
    exit()
else:
    print("Menu tidak tersedia!")  