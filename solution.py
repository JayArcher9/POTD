def colName(n):
    result = ""
    while n > 0:
        remainder = (n - 1) % 26
        result += chr(ord('A') + remainder)
        n = (n - 1) // 26
    return result


a = int(input("Enter the number: "))

b = colName(a)
print(b)
