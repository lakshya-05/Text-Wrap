import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)
    return "\n".join(a)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
