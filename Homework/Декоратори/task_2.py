# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def wrapper(name):
            string = func(name)
            for word in words:
                string = string.replace(word, '*')
            return string
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"