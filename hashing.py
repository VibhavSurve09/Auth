from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def verify_password(plain_password, hashed_password):
    """[summary]

    Args:
        plain_password (str): [Plain password]
        hashed_password (str): [Hashed password]

    Returns:
        [str]: [Returns boolean value true if passwords are right]
    """
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password):
    """[summary]

    Args:
        password (str): [Password to be hashed]

    Returns:
        [str]: [Hashed password]
    """
    return pwd_context.hash(password)