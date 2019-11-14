
# First Homework: N-first prime numbers
print('--------------------------------------------------')
N = int(input("How many first prime numbes you want to show: "))
nFound=0
num=2
while nFound<N:
    isPrime=1
    for i in range(2,num):
        if (num % i)==0:
            isPrime=0
            break
    if isPrime==1:
        nFound=nFound+1
        print(num)
    num=num+1



print('--------------------------------------------------')







if num == 1:
    print(num, "is not prime")
else:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, " is not a prime number")
            print(i, " times ", num // i, " is ", num)
            break
    else:
        print(num, " is prime")




# Homework 2: Count words in a file:

f = 'Texto1.txt'
with open(f, 'r') as infile:
    line = infile.readline()
    while line:
        print(line)
        line = infile.readline()


# Learning to use dictionaries:
