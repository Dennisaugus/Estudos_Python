"""
Escrevendo um iterador customizado


"""
# relembrando a função range()
for n in range(11):
    print(n)


class Contador:
    def __init__(self, menor, maior) :
       self.menor = menor
       self.maior = maior

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration

con = Contador(1,61)

print(con.menor)
print(con.maior)

it = iter(con)

# print(next(it))

for n in Contador(1, 61):
    print(n)

for n in range(1,61):
    print(n)