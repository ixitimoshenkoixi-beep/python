import math

def calculate_z(a, b):
    """
    Обчислює значення z за заданою умовою
    """
    if a >= 15:
        return math.sin(2 * a) + math.cos(2 * b)
    else:
        return math.sqrt(a + b ** 2)


def calculate_expression(n):
    """
    Обчислює значення виразу:
    (1.1)^(n/2) + 2/3 + 3/4 + ... + (n+1)/(n+2)
    """
    result = (1.1) ** (n / 2)

    for i in range(2, n + 2):
        result += i / (i + 1)

    return result


def main():
    # Ввід для першої функції
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))

    z = calculate_z(a, b)
    print(f"Значення z = {z:.6f}")

    # Ввід для другої функції
    n = int(input("Введіть натуральне число n: "))

    if n <= 0:
        print("Помилка: n має бути натуральним числом")
    else:
        value = calculate_expression(n)
        print(f"Значення виразу = {value:.6f}")


if __name__ == "__main__":
    main()
