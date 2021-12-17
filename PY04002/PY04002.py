class Rectangle:
    def __init__(self, a, b, color) -> None:
        self.perimeter = 2*(a+b)
        self.area = a*b
        self.color = color.title()
    
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print(r.perimeter, r.area, r.color)
else:
    print('INVALID')