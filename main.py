def to_upper(name):
    return name.to_upper()

def say_hello(name):
    print(f"name is, {name}")


if __name__="__main__":
    name="Yash"
    say_hello(name)
    up=to_upper(name)
    print(up)