def get_user(user_id):
    # SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)

# Division code
def divide(a, b):
    return a / b 

# factorial function
def factorial(num):
    fact  = 0
    while(num >=0):
        fact = fact * num
        num -=1

    return fact


def mul(num):
    return num * num

#multiplication