from functools import partial

def some_method(first: str, second: int, third: str=None, *args, option="got one", **kwargs):

    print(f"I am doing something with the first: {first}")

    print(f"here is the second param which is an int: {str(second)}")

    if third:
        print(f"We actually have a third: {third}")

    if args:
        for arg in args:
            print(f"Here is an arg: {str(arg)}")

    if option:
        print(f"Here is the option: {option}")

    if kwargs:
        for key, val in kwargs.items():
            print(f"The value of {key} is {val}")

def new_method_to_test_kwargs_and_partial(one, two, three, **kwargs):

    print(one) if one else None
    print(two) if two else None
    print(three) if three else None
    if kwargs:
        for key, val in kwargs.items():
            print(f"{key}: {val}")

# new_method = partial(new_method_to_test_kwargs_and_partial, "hello", "goodbye", "really", param1="yeah something else", param2="even more")

# new_method()

# some_method('hello', 25, 'goodbye', 3, 66, 99, 'yo momma', option='do we really got one', param1='something', param2='something else', param3='yo momma got something else')

newer_method = partial(new_method_to_test_kwargs_and_partial, "hello", "goodbye", "really")

newer_method()


