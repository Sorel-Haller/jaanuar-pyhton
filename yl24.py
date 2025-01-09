#UPC vöötkoodi kontrollsumma arvutamise ülesanne. 
# Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. Defineeri kontrollsumma arvutamise funktsioon.
# (https://www.w3schools.com/python/python_functions.asp)

def upc(n):
    n = [int(i) for i in str(n).zfill(11)]
    m = ((sum(n[::2]) * 3) + sum(n[1::2])) % 10
    return 10 - m if m != 0 else m