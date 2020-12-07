def say():
    print("")
    print("")
    print("Hello, World!")
    print("")
    print("")

def read_data():
    with open('../data/data.txt'. 'rt') as f:
        for line in f:
            print(line)