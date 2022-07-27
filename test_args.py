def test(*args, **kwargs):
    print(args)
    print(kwargs)
    new = f"{args}\n{kwargs}"
    print(new)
    print(type(new))


def main():
    test("first_string", second="second_string", third="third_string")

if __name__ == "__main__":
    main()
