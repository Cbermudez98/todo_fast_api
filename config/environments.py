import os
from dotenv import load_dotenv

load_dotenv()

parameter_store = {
    "HOST": os.environ["HOST"] if not None else "0.0.0.0",
    "PORT": os.environ["PORT"] if not None else 8080,
    "DB_USER": os.environ["DB_USER"] if not None else "test",
    "DB_PASSWORD": os.environ["DB_PASSWORD"] if not None else "test",
    "DB_NAME": os.environ["DB_NAME"] if not None else "test",
    "DB_PORT": os.environ["DB_PORT"] if not None else "test",
    "DB_HOST": os.environ["DB_HOST"] if not None else "test",
    "ENV": os.environ["ENV"] if not None else "Dev",
    "JWT_KEY": os.environ["JWT_KEY"] if not None else "test",
    "JWT_ALGORITHM": os.environ["JWT_ALGORITHM"] if not None else "test"
}