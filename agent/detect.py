LIMITS = {
    "cpu": 85,
    "mem": 90,
    "disk": 90,
    "net": 400
}

def check(data):
    flags = []
    for k in LIMITS:
        if data[k] > LIMITS[k]:
            flags.append(f"{k}:{data[k]}")
    return flags
