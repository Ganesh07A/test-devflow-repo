<<<<<<< HEAD
def get_user(user_id):
    # SQL injection 
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
=======
def get_user(user_id):
    # SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
>>>>>>> 9c126af4b3cb8843f8801a5f412b40bd16eb3e4b


# division code 
def divide(a, b):
    return a / b  
# Division code
def divide(a, b):
    return a / b 
