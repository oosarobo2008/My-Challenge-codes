# Question: find out if a number is prime number or not

def Primenumber(num):
# define a flag variable
  flag = False

# prime numbers are greater than 1
  if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
  if flag:
    return "This is not a prime number"
  else:
    return "This is a prime number"
# To take input from the user
num = int(input("Enter a number: "))
(T) = Primenumber(num)
print(T)