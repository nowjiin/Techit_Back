def angled_triangle():
    while True:
        triangle = list(map(int, input().split()))
        triangle.sort()
        if 0 in triangle:
            break

        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print("직각 삼각형 입니다.")
        else:
            print("직각 삼각형이 아닙니다")

angled_triangle()
