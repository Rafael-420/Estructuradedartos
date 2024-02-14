import os

os.system('cls' if os.name == 'nt' else 'clear')

fila = []

fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
fila.append('cliente4')

cliente_atendido = fila.pop(0)
print("", cliente_atendido)
print("fila despues de atender a un cliente son:",fila)

class cola:
    def ___init
