def angled_triangle(triangle):
    while True:
        if 0 in triangle:
            break

        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print("직각 삼각형 입니다.")
        else:
            print("직각 삼각형이 아닙니다")

tri_len = list(map(int, input().split()))
tri_len.sort()
angled_triangle(tri_len)
