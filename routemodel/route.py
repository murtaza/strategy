import googlemaps
from datetime import datetime
from routemodel.config import API_KEY


class Route(object):
    """
    This is a generic route given x, y.
    """


def main():
    gmaps = googlemaps.Client(key=API_KEY)



    pass


if __name__ == "__main__":
    main()

"""
The plan:
* Create a route using:
* Get the elevation by giving a path
""