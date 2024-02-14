import os
os.system('cls' if os.name == 'nt' else 'clear')

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("La cola está llena. No se puede agregar más elementos.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía. No se puede eliminar ningún elemento.")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def display(self):
        if self.is_empty():
            print("La cola está vacía.")
            return
        elif self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Ejemplo de uso
if __name__ == "__main__":
    capacity = 5
    cola = CircularQueue(capacity)

    cola.enqueue("chrome")
    cola.enqueue("visual estudio")
    cola.enqueue("word")
    cola.enqueue("Powerpoint")
    cola.enqueue("Microsoft Edge")

    print("Elementos abiertos:")
    cola.display()

    print("cerrando el programa:", cola.dequeue())
    print("Cerrando :", cola.dequeue())

    print("Elementos en la cola después de eliminar:")
    cola.display()

    cola.enqueue("Ventana6")
    cola.enqueue("Ventana7")

    print("Elementos en la cola después de agregar más elementos:")
    cola.display()
