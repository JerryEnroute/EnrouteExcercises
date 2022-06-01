from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle

print('Here i have a bunch of shapes:\n')

if __name__ == '__main__':

    square1 = Square('red', True, 5)
    print('My first square has sides of length',
    square1.getSide(), ', an area of', 
    square1.getArea(), ', a perimeter of', 
    square1.getPerimeter(), ', it is colored', 
    square1.getColor(), 'and it is', 'filled\n' 
    if square1.isFilled() else 'not filled\n')

    square2 = Square('blue', False, 10)
    print('My second square has sides of length', 
    square2.getSide(), ', an area of', 
    square2.getArea(), ', a perimeter of', 
    square2.getPerimeter(), ', it is colored', 
    square2.getColor(), 'and it is', 'filled\n' 
    if square2.isFilled() else 'not filled\n')

    rectangle1 = Rectangle('green', True, 7, 11)
    print('My first rectangle has a width of', 
    rectangle1.getWidth(), ', a length of', 
    rectangle1.getLength(), ', an area of', 
    rectangle1.getArea(), ', a perimeter of', 
    rectangle1.getPerimeter(), ', it is colored', 
    rectangle1.getColor(), 'and it is', 'filled\n' 
    if rectangle1.isFilled() else 'not filled\n')

    rectangle2 = Rectangle('red', False, 2, 5)
    print('My second rectangle has a width of', 
    rectangle2.getWidth(), ', a length of', 
    rectangle2.getLength(), ', an area of', 
    rectangle2.getArea(), ', a perimeter of', 
    rectangle2.getPerimeter(), ', it is colored', 
    rectangle2.getColor(), 'and it is', 'filled\n' 
    if rectangle2.isFilled() else 'not filled\n')

    circle1 = Circle('white', False, 4)
    print('My first circle has a radius of', 
    circle1.getRadius(), 'an area of',
    circle1.getArea(), ', a perimeter of', 
    circle1.getPerimeter(), ', it is colored', 
    circle1.getColor(), 'and it is', 'filled\n' 
    if circle1.isFilled() else 'not filled\n')

    circle2 = Circle('black', True, 8)
    print('My second circle has a radius of', 
    circle2.getRadius(), 'an area of',
    circle2.getArea(), ', a perimeter of', 
    circle2.getPerimeter(), ', it is colored', 
    circle2.getColor(), 'and it is', 'filled\n' 
    if circle2.isFilled() else 'not filled\n')

    triangle1 = Triangle('yellow', True, 3)
    print('My fisrt triangle has sides of length',
    triangle1.getSideLength(), 'an area of', 
    triangle1.getArea(), ', a perimeter of', 
    triangle1.getPerimeter(), ', it is colored', 
    triangle1.getColor(), 'and it is', 'filled\n' 
    if triangle1.isFilled() else 'not filled\n')

    triangle2 = Triangle('orange', True, 5)
    print('My second triangle has sides of length',
    triangle2.getSideLength(), 'an area of', 
    triangle2.getArea(), ', a perimeter of', 
    triangle2.getPerimeter(), ', it is colored', 
    triangle2.getColor(), 'and it is', 'filled\n' 
    if triangle2.isFilled() else 'not filled\n')