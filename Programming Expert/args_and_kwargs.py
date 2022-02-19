def get_args_and_kwargs(*args, **kwargs):
    number_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)

    if not isinstance(num, int) and not isinstance(num, float):
        return False 

    return number_of_args >= 4 and num > 5
