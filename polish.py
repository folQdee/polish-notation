"""Модуль для преобразования арифметических выражений в обратную польскую запись и их вычисления
Вот бы pylint сработал сейчас"""

def infix_to_rpn(expression):
    """Преобразует инфиксное выражение в обратную польскую запись (RPN)."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isdigit() or is_float(token):
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки")
            stack.pop()
        else:
            raise ValueError(f"Неизвестный токен: {token}")

    while stack:
        if stack[-1] in '()':
            raise ValueError("Несбалансированные скобки")
        output.append(stack.pop())

    return output


def is_float(token):
    """"Проверяет тип токена"""
    try:
        float(token)
        return True
    except ValueError:
        return False


def evaluate_rpn(rpn_tokens):
    """Считает выражение в RNP"""
    stack = []

    for token in rpn_tokens:
        if token.isdigit() or is_float(token):
            stack.append(float(token))
        elif token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.append(a / b)
        else:
            raise ValueError(f"Неверный токен в RPN: {token}")

    if len(stack) != 1:
        raise ValueError("Неверное выражение")

    return stack[0]


def main():
    """Главная функция"""
    expr = input("Введите арифметическое выражение: ")
    try:
        rpn = infix_to_rpn(expr)
        print("Обратная польская запись:", ' '.join(rpn))
        result = evaluate_rpn(rpn)
        print("Результат:", result)
    except (ValueError, ZeroDivisionError) as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
