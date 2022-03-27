import os
os.system("clear")

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, 10000000 + 1):

	if i%3 == 0 and i%5 == 0:
		print(str(i) + " FizzBuzz")
		fizzbuzz_count += 1

	elif i%3 == 0:
		print(str(i) + " Fizz")
		fizz_count += 1

	elif i%5 == 0:
		print(str(i) + " Buzz")
		buzz_count += 1

	else:
		print(i)

print("__________________________")
print("Fizz\tBuzz\tFizzBuzz")
print(str("{:,}".format(fizz_count)) + "\t" + str("{:,}".format(buzz_count)) + "\t" + str("{:,}".format(fizzbuzz_count)))


