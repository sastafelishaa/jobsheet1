import random
from guess import Tebak

hasil = Tebak()

hasil.jawaban = random.randint(1,10)

hasil.tebakan = int(input("Tebak angka 1 sd 10 : "))

if hasil.cek():
    print("Jawaban kamu benar!")
else :
    print("Jawaban kamu salah!")
