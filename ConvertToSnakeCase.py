def to_snake_case(s):
    return ''.join(['_' + ch.lower() if ch.isupper() else ch for ch in str(s)]).lstrip('_')


if __name__ == '__main__':
    print(to_snake_case(''))
    print(to_snake_case('a'))
    print(to_snake_case('A'))
    print(to_snake_case('aa'))
    print(to_snake_case('AA'))
    print(to_snake_case('aaa'))
    print(to_snake_case('AAA'))
    print(to_snake_case('snakeCase'))
    print(to_snake_case('theQuickBrownFox'))
