import geocoder
address = "1600 Pennsylvania Ave NW, Washington DC USA"
coordinates = geocoder.arcgis(address)
geo = geocoder.arcgis(address)
print(geo.latlng)
# output: [38.89767510765125, -77.03654699820865]

# If we want to retrieve the location from a set of coordinates
# perform a reverse query.
geocoder.arcgis([38.89767510765125, -77.03654699820865], method="reverse")

# output: <[OK] Arcgis - Reverse [White House]>
