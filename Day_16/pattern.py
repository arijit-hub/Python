## Importing necessary libraries ##

import numpy as np # for mathematical programming #

import matplotlib.pyplot as plt # for visualization #


## Creating  the Checkerboard pattern ##

## Creating the checker class ##

class Checker:

    def __init__(self, resolution, tile_size):

        assert (type(resolution) == int)
        self.resolution = resolution

        assert (type(tile_size) == int)
        self.tile_size = tile_size

        self.output = np.empty((resolution, resolution))

    def draw(self):
        '''
        Implements the diagram of the checkerboard.
        '''

        ## Check if the resololution and tile size are properly calibrated ##

        if self.resolution % (2 * self.tile_size) != 0:
            raise ValueError('Sorry! Please change the value of tile size.')

        else:

            ## Create the unit block of the checkerboard ##
            ## It is basically a 2 * 2 grid with alternative blacks and whites ##
            ## Generally we need to also take into consideration the number of pixels each black and white... ##
            ## ...cover based on the tile size and repeat it in both the axis to make the unit block based...##
            ## ...on tile size ##

            unit_block = np.repeat(np.repeat(np.array([[0, 1], [1, 0]]), self.tile_size, axis=0),
                                   self.tile_size, axis=1)

            ## Repeat the unit block to resolution // (2 * self.tile_size) to get the checkerboard pattern ##

            self.output = np.tile(unit_block, (int(self.resolution // (2 * self.tile_size)),
                                               int(self.resolution // (2 * self.tile_size))))

            return np.copy(self.output)

    def show(self):
        '''
        Displays the checkerboard pattern.
        '''

        ## Displaying the checkerboard pattern ##

        plt.imshow(self.output, cmap='gray')
        plt.show()

    ## Creating  the Circle mask ##

    ## Creating the circle class ##


class Circle:

    def __init__(self, resolution, radius, position):
        assert (type(resolution) == int)
        self.resolution = resolution
        assert (type(radius) == int)
        self.radius = radius

        ## Breaking down the position tuple ##

        assert (type(position) == tuple)
        self.center_y, self.center_x = position

        self.output = np.zeros((self.resolution, self.resolution))

    def draw(self):
        '''
        Implements the diagram of the circle.
        '''

        ## The circle is drawn with x and y coordinates varying between (x_center - radius , x_center + radius) ...##
        ## ... and (y_center - radius , y_center + radius). These are defined next. ##

        xval = np.linspace(self.center_x - self.radius, self.center_x + self.radius, num = self.radius * 2 + 1 , dtype=int)
        yval = np.linspace(self.center_y - self.radius, self.center_y + self.radius, num = self.radius * 2 + 1 , dtype=int)

        ## Create the grid of points with the xval and the yval. These will help to index at the specific location...##
        ## ...of the output image. ##

        x_v, y_v = np.meshgrid(xval, yval)

        ## Define threshold by checking if the x^2 + y^2 <= radius^2 ##

        threshold = (np.square(x_v - self.center_x) + np.square(y_v - self.center_y) - (self.radius ** 2)) <= 0.0

        self.output[x_v[threshold], y_v[threshold]] = 1.

        return self.output.copy()

    def show(self):
        '''
        Displays the checkerboard pattern.
        '''

        plt.imshow(self.output, cmap='gray')
        plt.show()


class Spectrum:

    def __init__(self, resolution):
        assert (type(resolution) == int)
        self.resolution = resolution

        self.output = np.zeros((self.resolution, self.resolution, 3))

    def draw(self):
        ## The red is aligned to the right side of the colour spectrum. Hence align it with a gradual increase...##
        ## ...from left to right. ##

        self.output[:, :, 0] = np.linspace(0., 1., num=self.resolution)

        ## The green is aligned to the bottom side of the colour spectrum. Hence align it with a gradual increase...##
        ## ...from bottom to up. ##

        self.output[:, :, 1] = np.repeat(np.expand_dims(np.linspace(0., 1., num=self.resolution), 1)
                                         , self.resolution).reshape(self.resolution, self.resolution)

        ## The blue is aligned to the left side of the colour spectrum. Hence align it with a gradual decrease...##
        ## ...from left to right. ##

        self.output[:, :, 2] = np.linspace(1., 0., num=self.resolution)

        return self.output.copy()

    def show(self):
        plt.imshow(self.output)
        plt.show()

s = Circle(512  , 100 , (250 , 250))
s.draw()
s.show()