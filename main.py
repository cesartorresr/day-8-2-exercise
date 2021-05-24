#Write your code below this line 👇
#Los números primos son divisibles por 1 y por ellos mismos. Toca hacer un loop que compruebe que sea solo divisible por el mismo o por uno. Contando desde el número 2 hasta un número antes de él mismo. Si el modulo es igual a 0 quiere decir que NO es Primo.
def prime_checker(number):
  prime_number = True
  for i in range(2, number):
    if number % i == 0:
      prime_number = False
  if prime_number:
    print("It's prime")
  else:
    print("It's not prime")         




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



