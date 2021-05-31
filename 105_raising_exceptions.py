def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - user")

a = increment('df364')
print(a)
print("ss")