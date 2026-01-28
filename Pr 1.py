import time

start_time = time.time()
target = 1000000
p = [1]
n = 1

while True:
    res = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        
        if g1 <= n:
            if k % 2 == 1:
                res += p[n - g1]
            else:
                res -= p[n - g1]
        else:
            break
            
        if g2 <= n:
            if k % 2 == 1:
                res += p[n - g2]
            else:
                res -= p[n - g2]
        else:
            break
        k += 1
        
    res %= target
    if res == 0:
        break
    p.append(res)
    n += 1

end_time = time.time()

print(f"Результат n: {n}")
print(f"Время выполнения: {end_time - start_time:.4f} сек.")