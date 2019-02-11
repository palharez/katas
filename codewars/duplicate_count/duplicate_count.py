def duplicate_count(text):
    count = 0
    text = text.lower()
    for n in text:
        if text.count(n) > 1:
            count += 1
            text = text.replace(n, '')
    return count


if __name__ == "__main__":
    print(duplicate_count("abcdea"))
