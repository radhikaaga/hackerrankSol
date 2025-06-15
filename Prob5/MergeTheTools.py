def merge_the_tools(s, k):
    # Split the string into substrings of size k
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        result = ""
        for ch in substring:
            if ch not in result:
                result += ch
        print(result)

# Example usage
if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s, k)
