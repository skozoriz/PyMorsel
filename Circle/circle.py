import math

class Circle:

    def __init__(self, *R):
        if len(R)== 0:
            rds = 1
        else:
            rds = R[0]
        self.radius = rds
        #self.diameter = 2 * rds
        #self.area = math.pi * (rds ** 2)

    def __setattr__(self, name, value):
        if name == 'radius':
            if value < 0 :
                raise ValueError("Radius cannot be negative")
            self.__dict__['radius'] = value
            self.__dict__['diameter'] = 2 * value
            self.__dict__['area'] = math.pi * (value ** 2)
        elif name == 'diameter':
            self.__dict__['radius'] = value / 2
            self.__dict__['diameter'] = value
            self.__dict__['area'] = math.pi * ((value/2) ** 2)
        elif name == 'area':
            raise AttributeError(name)

    def __repr__(self):
        return f'Circle({self.radius})'


if __name__ == '__main__':
    
    c5 = Circle(5)
    print(c5, c5.radius, c5.diameter, c5.area)
    c1 = Circle()
    print(c1, c1.radius, c1.diameter, c1.area)
    
    c5.radius = 1
    print(c5, c5.radius, c5.diameter, c5.area)
    c5.diameter = 10
    print(c5, c5.radius, c5.diameter, c5.area)
   
    try:
        c5.area = 1000
    except AttributeError:
        print('Area setting is not allowed!')
        print(c5, c5.radius, c5.diameter, c5.area)