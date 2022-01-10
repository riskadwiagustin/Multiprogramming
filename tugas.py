#5200411006 Hamdan Fajril Haqiqie
#52004110023 Adi Wijaya
#5200411031 Riska Dwi Agustin
#5200411413 Juan Fredrick Pandia


print("="*50)
print("MANAJEMEN MEMORI - MULTIPROGRAMING")
print("="*50)
ram = int(input("Kapasitas RAM : "))
so = int(input("Sistem Operasi yang dipakai : "))
program1 = int(input("Kapasitas Program 1 : "))
program2 = int(input("Kapasitas Program 2 : "))
program3 = int(input("Kapasitas Program 3 : "))

totalprogram = (program1 + program2 + program3)

sisa = (ram - (so + totalprogram))


print("="*50)
print("Output")
print("_"*50)
print("Kapasitas ram\t\t= ",ram,"GBps")
print("Sistem Operasi yang dipakai\t= ",so,"GBps")
print("Kapasitas Program 1\t\t=",program1,"GBps")
print("Kapasitas Program 2\t\t=",program2,"Gbps")
print("Kapasitas Program 3 \t\t=",program3,"Gbps")
print("Total Kapasitas program 1-3\t=",totalprogram,"Gbps")
print("Sisa Kapasitas nya adalahhh\t=",sisa,"Gbps")