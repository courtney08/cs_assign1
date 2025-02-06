def rounded(func):
    def wrapper(*args):
        result = func(*args)
        rounded_result = round(result)
        print("after calling the function", rounded_result)
        return rounded_result
    return wrapper


@rounded
def add(x,y):
    unrounded_result = x+y
    print("inside the function:", unrounded_result)
    return unrounded_result

add(9.1,10.1)