from datetime import datetime, timezone
from time import sleep
import uuid


n = uuid.uuid4()

while True:
    now = datetime.now(timezone.utc)
    formatted_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    print(formatted_time + ":", n)
    sleep(5)
