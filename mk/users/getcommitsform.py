def getcommitsform(count):
    if count % 100 in (11, 12, 13, 14): return f"{count} правок"
    if count % 10 == 1: return f"{count} правку"
    if count % 10 in (2, 3, 4): return f"{count} правки"
    if count == 0: return "правок... 0"
    return f"{count} правок"
