def sieve_of_Eratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2

    while p*p < num:

        if prime[p] == True:
            for i in range(p*p, num + 1, p):
                prime[i] = False
        p += 1
    
    for i in range(2, num + 1):
        if prime[i] == True:
            print(i, end=" ")
            
sieve_of_Eratosthenes(45)
    

