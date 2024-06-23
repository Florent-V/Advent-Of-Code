import time


now = time.time()

compteur = 1
for i in range(1000000000):
    compteur += 1
print(time.time() - now)

