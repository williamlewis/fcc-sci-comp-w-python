class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        output = f'Rectangle(width={self.width}, height={self.height})'
        return output
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal

    def get_picture(self):
        if (self.width > 50) or (self.height > 50):
            return 'Too big for picture.'
        else:
            picture = ''
            for i in range(0, self.height):
                picture += ('*' * self.width) + '\n'
            return picture
    
    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        amount_inside = width_fit * height_fit

class Square:
    def __init__(self, side_len):
        self.width = side_len
        self.height = side_len
    
    def __str__(self):
        output = f'Square(side={self.width})'
        return output
    
    def set_side(self, new_side_len):
        self.width = new_side_len
        self.height = new_side_len
