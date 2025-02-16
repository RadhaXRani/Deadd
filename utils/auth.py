from config import PAID_USERS

def is_paid_user(user_id):
    return user_id in PAID_USERS
