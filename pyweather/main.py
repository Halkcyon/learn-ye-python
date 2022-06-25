def greet_person(f):
    def wrapper():
        rv = f()

        print(rv, "world")

    return wrapper


@greet_person
def say_hello():
    return "hello"


wrapped_function = greet_person(say_hello)


class App:
    routes: dict

    def get(self, f, route, *args, **kwd):
        self.routes[route] = f


import bs4
import requests
import rich

res = requests.get("http://localhost:8000")
if res.ok:
    body = res.json()
    if "world" in body["message"]:
        print("successful call")
else:
    print("houston, we have a problem")


res = requests.get("https://fastapi.tiangolo.com")
soup = bs4.BeautifulSoup(res.content)
