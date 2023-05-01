def deco_html(func):
    def wrapper(*args, **kwargs):
        res = '<html>'
        res = res + func(*args, **kwargs)
        res = res + '</html>'
        return res
    return wrapper


def deco_body(func):
    def wrapper(*args, **kwargs):
        res = '<body>'
        res = res + func(*args, **kwargs)
        res = res + '</body>'
        return res
    return wrapper


@deco_html
@deco_body
def test(x):
    return x


print(test("HELLO"))
