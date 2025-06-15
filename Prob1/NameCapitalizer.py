def capitalize_name(full_name):
    # Split the name into words
    words = full_name.split()
    # Capitalize the first character if it's a letter, leave as is if it's a number
    capitalized_words = [word[0].upper() + word[1:] if word and word[0].isalpha() else word for word in words]
    # Join and return
    return ' '.join(capitalized_words)

# Read input
if __name__ == "__main__":
    full_name = input()
    print(capitalize_name(full_name))
