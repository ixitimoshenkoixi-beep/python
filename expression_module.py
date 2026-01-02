def calculate_expression(n):
    """
    Обчислює значення виразу:
    (1.1)^(n/2) + 2/3 + 3/4 + ... + (n+1)/(n+2)
    """
    if n <= 0:
        raise ValueError("n має бути натуральним числом")

    result = (1.1) ** (n / 2)

    for i in range(2, n + 2):
        result += i / (i + 1)

    return result
