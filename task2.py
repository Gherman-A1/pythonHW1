# Найдите сумму цифр трехзначного числа 123 -> 6 (1 + 2 + 3); 100 -> 1 (1 + 0 + 0)
n=int(input("введите трехзначное число: "))
res=0
while n>9:
    res=res+n%10
    n=n//10
res=res+n
print(res)