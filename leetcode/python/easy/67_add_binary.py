def add_binary(a: str, b: str) -> str:
    result = int(a, 2) + int(b, 2)
    result = bin(result)
    return result[2:]


if __name__ == "__main__":
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
