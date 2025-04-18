print(bool('Kodnest'))#True
#print(int('Kod')) #Error
print(int('30')) #30
#print(float('Kodnest')) #Error
print(float('22.23')) #22.23
print(bool("")) #False
print(bool(0)) # False
print(bool(12)) # True
#print(int('12.56')) #Error
print(int(12.56)) #12

value = int(float(input('Enter floting point number: ')))
print(value, type(value))