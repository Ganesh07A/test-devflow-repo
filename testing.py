

# division code 
def divide(a, b):
    return a / b 


def get_user(user_id):
    # SQL injection 
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query) 


def mul(num):
    mul = num * num