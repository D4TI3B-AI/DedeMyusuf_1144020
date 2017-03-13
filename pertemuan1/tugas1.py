import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa palembang")
b = input("Masukan Nilai 1: ")
a = input("Masukan Nilai 2: ")
e = input("Masukan Nilai 3: ")
k = input("Masukan Nilai 4: ")


if b == 'sikok':
	b=1

if b == 'duo':
	b=2

if b == 'tigo':
	b=3

if b == 'empat':
	b =4

if b == 'limo':
	b=5

if b == 'enam':
	b=6

if b == 'tujuh':
	b=7

if b == 'delapan':
	b=8

if b == 'sambilan':
	b=9

if b == 'nol':
	b=0

if a == 'sikok':
	a=1

if a == 'duo':
	a=2

if a == 'tigo':
	a=3

if a == 'empat':
	a=4

if a == 'limo':
	a=5

if a == 'enam':
	a=6

if a == 'tujuh':
	a=7

if a == 'delapan':
	a=8

if a == 'sambilan':
	a=9

if a == 'nol':
	a=0


if e == 'sikok':
	e=1

if e == 'duo':
	e=2

if e == 'tigo':
	e=3

if e == 'empat':
	e=4

if e == 'limo':
	e=5

if e == 'enam':
	e=6

if e == 'tujuh':
	e=7

if e == 'delapan':
	e=8

if e == 'sambilan':
	e=9

if e == 'nol':
	e=0


if k == 'sikok':
	k=1

if k == 'duo':
	k=2

if k == 'tigo':
	k=3

if k == 'empat':
	k=4

if k == 'limo':
	k=5

if k == 'enam':
	k=6

if k == 'tujuh':
	k=7

if k == 'delapan':
	k=8

if k == 'sambilan':
	k=9

if k == 'nol':
	k=0

jumlah = (b+a*e/k)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))