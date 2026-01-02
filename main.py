from expression_module import calculate_expression

def main():
    try:
        n = int(input("Введіть натуральне число n: "))
        value = calculate_expression(n)
        print(f"Значення виразу = {value:.6f}")
    except ValueError as e:
        print("Помилка:", e)

if __name__ == "__main__":
    main()
