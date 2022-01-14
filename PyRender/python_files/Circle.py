import math

class Circle:
    def __init__(self, radius, pos_x, pos_y, color):
        self.RADIUS = radius
        self.COLOR = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.last_x = self.pos_x
        self.last_y = self.pos_y

        self.current_pixel = self.calc_adjecent_pixels(self.RADIUS, self.pos_x, self.pos_y)
        self.last_pixel = self.current_pixel

    def calc_adjecent_pixels(self, radius, pos_x, pos_y):
        # calculate the adjacent Pixels belonging to the circle
        # Creates a list with the coordinates of all pixels with a distance of less or equal then the radius
        # Calculate with:
        #
        # pos_x +- m , posy +- n  -> n = { -radius, . . . , radius}
        #                         -> m = r -n
        #
        # pos_x, pos_y describe the center pixel of the circle
        list_of_adjacent_pixels = []
        x_diff = 0
        y_diff = 0
        for i in range(pos_y - radius, pos_y + 1):
            y_diff = abs(i - pos_y)
            for n in range(pos_x - radius, pos_x + 1):
                if (math.sqrt((n - pos_x) ** 2 + (i - pos_y) ** 2)) <= radius :
                    list_of_adjacent_pixels.append((n, i))
                    list_of_adjacent_pixels.append((n, pos_y + pos_y - i))
                    list_of_adjacent_pixels.append((pos_x + pos_x - n, i))
                    list_of_adjacent_pixels.append((pos_x + pos_x - n, pos_y +pos_y - i))


        return list_of_adjacent_pixels

    def move_circle(self, new_x, new_y):
        self.last_x = self.pos_x
        self.last_y = self.pos_y

        self.pos_x = new_x
        self.pos_y = new_y

        self.last_pixel = self.current_pixel
        self.current_pixel = self.calc_adjecent_pixels(self.RADIUS, self.pos_x, self.pos_y)