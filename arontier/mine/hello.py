def say():
    print("")
    print("")
    print("Hello, World!")
    print("")
    print("")


def read_data():
    import os
    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if 'data.txt' in file:
                fn = os.path.join(r, file)
    with open(fn, 'rt') as f:
        for line in f:
            print(line)
