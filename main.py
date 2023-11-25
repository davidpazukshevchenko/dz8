def raise_to_the_degrees(number, max_degree):
    i = 1
    for _ in range(max_degree):
        yield number**i
        i += 1


res = raise_to_the_degrees(2, 1000)
print(res)
for _ in res:
    print(_)
