def draw_pattern(n):
    current = n
    while current >= 1:
        print("*" * current)
        current = current - 1
        
    current = 2
    while current <= n:
        print("*" * current)
        current = current + 1

draw_pattern(4)

