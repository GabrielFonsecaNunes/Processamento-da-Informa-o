n = int(input())
soma = float(0)

try:
    for i in range(n):
        soma += float(input())

    print(f"Total: {soma:.2f}")
except Exception as e:
    raise e