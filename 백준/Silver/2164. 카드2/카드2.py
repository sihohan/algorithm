from queue import Queue


n = int(input())

cards = Queue()
for i in range(1, n + 1):
    cards.put(i)

while cards.qsize() > 1:
    cards.get()
    cards.put(cards.get())

print(cards.get())
