import random
a=random.randint(1,100)
while True: 
  b=int(input("Tahmin ettiğin sayıyı söyle: "))
  if a==b:
    print("Bildin!")
    break
  elif a>b:
    print("Daha büyük")
  else:
    print("Daha küçük")
