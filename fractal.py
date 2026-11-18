def draw_pattern(n):
    if n <= 1:
        print("*")
        return
    print("*" * n)
    draw_pattern(n - 1)
    print("*" * n)

draw_pattern(4)
