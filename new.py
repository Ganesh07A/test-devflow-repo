def fact(num) :
    fact = 0
    while num !=0:
        fact *= num
        num -=1

    print(f"factorial: ", fact)