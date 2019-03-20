def add_binary(a, b):
    return bin(a + b).replace("0b", "")

if __name__ == "__main__":
    print(add_binary(1, 1))