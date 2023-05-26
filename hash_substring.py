def read_input():

    input_type = input().lower()

    if "i" in input_type:

        pattern = input()
        text = input()
    elif "f" in input_type:
        filename = "06"
        with open(f"tests/{filename}", 'r') as file:
            pattern = file.readline()
            text = file.readline()
    else:
        raise Exception("Unknown command")

    return pattern.rstrip(), text.rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def calculate_hash(string):
    hash_value = 7
    for char in string:
        hash_value += ord(char)
        hash_value *= 37

    return hash_value


def get_occurrences(pattern, text):
    occurrences = []
    pattern_hash = calculate_hash(pattern)

    for i in range(len(text) - len(pattern) + 1):
        text_part = text[i:i + len(pattern)]
        current_hash = calculate_hash(text_part)

        if current_hash == pattern_hash:
            occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    occurrences = get_occurrences(*read_input())
    print_occurrences(occurrences)
