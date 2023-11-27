num = input("Limit: ")
i = 1

while (i <= int(num)) :
     if int(i) % 3 == 0 and int(i) % 5 == 0:
          print("FizzBuzz")
     elif int(i) % 3 == 0:
          print("Fizz")
     elif int(i) % 5 == 0:
          print("Buzz")
     else:
          print(i)
     i = i + 1