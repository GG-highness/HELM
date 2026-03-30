import os

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://helm:helm@localhost:3306/helm",
)
