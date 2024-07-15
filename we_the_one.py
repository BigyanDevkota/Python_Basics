# ygsjaauksak

# A default function for Prime checking conditions  
def PrimeChecker(a):  
    # Checking that given number is more than 1  
    if a > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(a/2) + 1):  
            # If the given number is divisible or not  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
        # Else it is a prime number  
 
