pi = 3.141592

def circle_area(r):
    return round(r**2*pi, 3)

radius = float(input('radius : '))

area = circle_area(radius)

print('area = %.3f'%(area))