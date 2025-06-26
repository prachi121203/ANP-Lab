Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> number = 3
 
    if number <= 1:
        print(f"{number} is not a prime number.")
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
   
       if is_prime:
           print(f"{number} is a prime number.")
       else:
           print(f"{number} is not a prime number.")
