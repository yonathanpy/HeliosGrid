import psutil

def snapshot():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "mem": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "net": len(psutil.net_connections())
    }
