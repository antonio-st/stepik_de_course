# Создайте функцию is_balanced_parentheses(s: str) -> bool, которая проверяет, сбалансированы ли скобки в строке
# (каждая открывающая скобка имеет соответствующую закрывающую).

input_str = input().replace("\"", "").replace(" ", "")

def is_balanced_parentheses(s: str) -> bool:
    acc = []

    for char in s:
        if char in ["(", "{", "["]:
            acc.append(char)
        else:
            if not acc:
                return False
            current_char = acc.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if acc:
        return False
    return True

print(is_balanced_parentheses(input_str))

# преподаватель

def is_balanced_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []

# Вызов функции
result = is_balanced_parentheses("([{}])")
print(result)  # True

# еще вариант
def is_balanced_parentheses(s: str) -> bool:
    scobs = {'(': ')', '[': ']', '{': '}'}
    for x in s:
        if x in scobs:
            if scobs[x] not in s:
                return False
    return True

print(is_balanced_parentheses(input()))