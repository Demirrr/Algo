# Implement the decorator 'debug' so that it displays the name
# of the decorated function before executing it:

# INSERT CODE HERE
def debug(f):
    def wrapper(*args,**kwargs):
        print(f.__name__)
        return f(*args,**kwargs)
    return wrapper

#@debug
def say(name):
    print("Name =", name)


say = debug(say)

say("DeepL")  # say: Name = DeepL
say("Linguee")  # say: Name = Linguee