def get_user(user_id):
    # SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)

# Division code
def divide(a, b):
    return a / b  # What if b is 0?


def mul(num):
    return num * num