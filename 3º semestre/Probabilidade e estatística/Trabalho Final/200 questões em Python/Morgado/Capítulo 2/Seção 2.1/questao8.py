def count_divisors(n):
    divisor_count = 0
    even_divisor_count = 0
    
    for i in range(1, n//2 + 1):
        if n % i == 0:  
            divisor_count += 1
            if i % 2 == 0: 
                even_divisor_count += 1
    
    divisor_count += 1
    if n % 2 == 0:  
        even_divisor_count += 1
    
    return divisor_count, even_divisor_count

number = 360
total_divisors, even_divisors = count_divisors(number)
print("Número total de divisores de", number, ":", total_divisors)
print("Número total de divisores pares de", number, ":", even_divisors)
