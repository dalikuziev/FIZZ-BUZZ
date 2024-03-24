print("FIZZ, BUZZ and FIZZBUZZ o'yiniga xush kulibsiz")
number = int(input("1 dan boshlab nechigacha sanaymiz: "))
fizz = []
n = 0
for number in range(1, number + 1):
  if number % 3 == 0 and number % 5 == 0:
    number = "FIZZBUZZ"
    fizz.append(number)
    n += 1
  elif number % 3 == 0:
    number = "FIZZ"
    fizz.append(number)
    n += 1
  elif number % 5 == 0:
    number = "BUZZ"
    fizz.append(number)
    n += 1
  print(number)
print(f"Bu o'yinda jami {n}ta FIZZ, BUZZ yoki FIZZBUZZ ishlatildi")
th = int(input(f"Nechanchi FIZZ, BUZZ yoki FIZZBUZZ ni bilishni xohlaysiz "
               f"(1 dan {n} gacha bo'lgan 1ta son kiriting): "))
print(f"{th}-o'rinda {fizz[th - 1]} turibdi.")
