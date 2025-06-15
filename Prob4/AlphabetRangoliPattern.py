def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    # Create the pattern lines
    lines = []
    for i in range(size):
        # Left and right parts of the row
        left = alphabet[size-1:i:-1]  # descending
        center = alphabet[i:size]     # ascending
        row = '-'.join(left + center)
        lines.append(row.center(4*size - 3, '-'))

    # Full rangoli: top + center + bottom
    full_rangoli = lines[::-1] + lines[1:]
    for line in full_rangoli:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
