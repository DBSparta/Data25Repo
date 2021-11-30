class Location:
    def __init__(self, latitude, longitude, name = "bham"):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location=({self.longitude}, latitude={self.latitude})"

    # def __str__(self, string):
    #     return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(bham_academy)