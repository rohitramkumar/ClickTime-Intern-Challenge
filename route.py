from googleplaces import GooglePlaces
import googlemaps
import os

# Longtitude and latitude of ClickTime office.
CLICKTIME_COORD = {'lat': 37.785636, 'lng': -122.397119}
# My API Key
API_KEY = "AIzaSyDp_28jsWT6nFsYpIFQYrgje_WT740R97k"

def getRoute(user_location, rankby, mode):
	# Init API Clients
	google_places = GooglePlaces(API_KEY)
	google_maps = googlemaps.Client(key=API_KEY)

	# Get the coordinates of the nearest donut shop to the ClickTime office.
	query_result = google_places.nearby_search(
        	lat_lng=CLICKTIME_COORD,
        	name='donut',
        	types='food',
        	rankby='distance')

	# Retrieve the name and coordinates of the nearest shop.
	shop_name = query_result.places[0].name
	shop_coord = query_result.places[0].geo_location

	# Get the current user location


	# Get directions from the users current location to the 
	# donut shop. For some reason, the Google Maps API does
	# not allow you to use waypoints when asking for public
	# transportation for a route. Therefore, I will have
	# to break the route into two different pieces.
	directions_result = google_maps.directions(user_location,
		shop_coord, )
