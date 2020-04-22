import os

MODEL_PATH = os.path.join("./checkpoints", '0model_best.pth.tar')

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_NAME")

connection_string = "mysql+mysqldb://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)

print(connection_string)
