import time
from metrics import snapshot
from detect import check
from push import send

while True:
    data = snapshot()
    alerts = check(data)
    send({"data": data, "alerts": alerts})
    time.sleep(5)
