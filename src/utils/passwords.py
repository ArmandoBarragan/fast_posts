import bcrypt

def hash_password(password: str) -> str:
    """
    Hashes the password so that it gets stored in the database
    :param password: str
    :return: str
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(password, hashed_password)-> bool:
    """
    Checks if the given password matches the hashed password
    :param password: str
    :param hashed_password: str
    :return:
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))