class Coordinate:
    def __init__(self, x_val, y_val):
        """
        Constructor that initializes the coordinate with x and y values.
        :param x_val: X coordinate value
        :param y_val: Y coordinate value
        """
        self.x_val = x_val
        self.y_val = y_val

    def __str__(self):
        """
        Returns a string representation of the coordinate.
        :return: String in the format (x_val, y_val)
        """
        return f"({self.x_val},{self.y_val})"

    def __repr__(self):
        """
        Returns a string representation for use in lists.
        :return: String in the format (x_val, y_val)
        """
        return self.__str__()

    @property
    def distance_from_origin(self):
        """
        Calculates the distance from the origin.
        :return: Distance from the origin
        """
        dist_squared = (self.x_val) ** 2 + (self.y_val) ** 2
        distance = dist_squared ** 0.5
        return distance

    def __gt__(self, other):
        """
        Compares two coordinates based on their distance from the origin.
        :param other: Another coordinate instance
        :return: True if this coordinate is further from the origin than the other
        """
        my_distance = self.distance_from_origin
        other_distance = other.distance_from_origin
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Checks if two coordinates are equidistant from the origin.
        :param other: Another coordinate instance
        :return: True if both are equidistant from the origin
        """
        return self.distance_from_origin == other.distance_from_origin


if __name__ == "__main__":
    # Create random coordinates
    import random
    coordinates_list = []
    for _ in range(5):
        coordinates_list.append(Coordinate(random.randint(1, 99), random.randint(1, 99)))

    print(coordinates_list)  # Prints the list of coordinates

    for coordinate in coordinates_list:
        print(coordinate.distance_from_origin)

    coord_a = Coordinate(2, 3)
    coord_b = Coordinate(7, 9)
    print(coord_a.distance_from_origin > coord_b.distance_from_origin)
    print(coord_a > coord_b)

    coordinates_list.sort()
    print(f"The coordinate furthest from origin is: {coordinates_list[-1]} and the closest coordinate is: {coordinates_list[0]}")
