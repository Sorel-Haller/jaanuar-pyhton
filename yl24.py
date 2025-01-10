#UPC vöötkoodi kontrollsumma arvutamise ülesanne. 
# Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. Defineeri kontrollsumma arvutamise funktsioon.
# (https://www.w3schools.com/python/python_functions.asp)

def upc(n):
    m = ((sum(n[::2]) * 3) + sum(n[1::2])) % 10
    return 10 - m if m != 0 else m

print(upc(3600029145))