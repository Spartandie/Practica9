from collections import namedtuple

planeta=namedtuple('planeta', ['nombre', 'numero'])
planeta1=planeta('Mercurio', 1)
print(planeta1)
planeta2=planeta("Venus",2)
print(planeta2)
print(planeta1.nombre, planeta2.nombre)
print(planeta2[0], planeta2[1])