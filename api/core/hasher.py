from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    if not pwd_context.verify(plain_password, hashed_password):
        return False
    return True