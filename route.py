from googleplaces import GooglePlaces
from googlemaps import Client

import os

# Longtitude and latitude of ClickTime office.
CLICKTIME_LOCATION = {'lat': 37.785636, 'lng': -122.397119}

# My API Key
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

def getDirections(current_location, transportation_mode, shop_preference):
  """Return a list of directions that the user should take to
    get from their current location to the ClickTime office while
    stopping for donuts and coffee along the way."""

  # Init API Clients
  google_places = GooglePlaces(GOOGLE_API_KEY)
  google_maps = Client(key=GOOGLE_API_KEY)

  # Get the coordinates of the nearest donut shop to the ClickTime office.
  query_result = google_places.nearby_search(
      lat_lng=CLICKTIME_LOCATION,
      name='donut',
      types='food',
      rankby=shop_preference)

  donut_shop_name = query_result.places[0].name
  donut_shop_location = query_result.places[0].geo_location

  # Get directions from current location to donut shop.
  # Had issues with waypoints so I broke the route into
  # two different pieces.
  directions_api_result = google_maps.directions(
      current_location,
      donut_shop_location, 
      mode=transportation_mode)

  directions = []
  for step in directions_api_result[0]['legs'][0]['steps']:
    directions.append(step['html_instructions'])
  directions.append('<font color="green">Arrived at ' 
      + donut_shop_name + '!</font>')

  # Get directions from the donut shop to the ClickTime office.
  directions_api_result = google_maps.directions(
      donut_shop_location,
      CLICKTIME_LOCATION, mode=transportation_mode)

  for step in directions_api_result[0]['legs'][0]['steps']:
    directions.append(step['html_instructions'])  
  directions.append('<font color="green">Arrived at ClickTime!</font>')
  
  return directions
