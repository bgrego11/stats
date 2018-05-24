from geopy.geocoders import Nominatim
from geopy import distance
import ssl

# Disable SSL certificate verification 
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

gl = Nominatim()
inputA = "greensboro nc"
cityA = (gl.geocode(inputA).latitude, gl.geocode(inputA).longitude)

inputB = "charlotte nc"
cityB = (gl.geocode(inputB).latitude, gl.geocode(inputB).longitude)

d = distance.distance(cityA,cityB).miles

print (d)
