DATA = []

def add(entry):
    DATA.append(entry)

def latest(n=50):
    return DATA[-n:]
