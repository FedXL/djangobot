import datetime

import jwt

from djangobot.config import SECRET

if __name__ == "__main__":

    print(datetime.datetime.utcnow())
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImZlZHhsIiwiZXhwIjoxNjk1NTQ3OTk0LjI3NDYyNiwibm93IjoxNjk1NTQ0Mzk0LjI3NDYyNn0.z-wpIs6XXyogufQSKFIh7bI3o889SnNAaGvTbz7SS9g"
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    print(payload)
    print(datetime.datetime.utcnow())