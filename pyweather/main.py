


def greet_person(f):
    def wrapper():
        rv = f()

        print(rv, "world")

    return wrapper



@greet_person
def say_hello():
    return "hello"


wrapped_function = greet_person(say_hello)


say_hello()



class App:
    routes: dict

    def get(self, f, route, *args, **kwd):
        self.routes[route] = f
