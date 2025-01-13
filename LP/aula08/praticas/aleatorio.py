import random


print(random.randint(1, 10))

coisas = ['microfone', 'banana', 'chapeu', 'bota']
print(random.choice(coisas))

print(random.sample(coisas, 2))

print(coisas)
random.shuffle(coisas)
print(coisas)
