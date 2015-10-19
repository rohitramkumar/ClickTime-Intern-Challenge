/*
* Credit to the link below for the idea on how to get a users current location.
* http://toddmotto.com/using-html5-geolocation-to-show-current-location-with-google-maps-api/
*/

/**
* The default user location. Currently Champaign, IL.
*/
var DEFAULT_USER_LOCATION = {'lat' : 40.1163889, 'lng' : -88.2433333}

/**
* Retrieve the user's location. In the case that geolocation is not
* available or the user blocks it, set to a default
* of Champaign, IL.
*/
function getLocation() { 
  if(!!navigator.geolocation) {		
    initAndOpenDialog(); 
    navigator.geolocation.getCurrentPosition(function(position) {	
      $('#dialog').dialog('close');			
	    fillFormWithCoordinates(position.coords.latitude,
		      position.coords.longitude);			
	  }, function(error) {
      $('#dialog').dialog('close');
      alert('You blocked geolocation. Using default location of Champaign, IL.')
		  fillFormWithCoordinates(DEFAULT_USER_LOCATION['lat'],
		      DEFAULT_USER_LOCATION['lng']);
	  });
	} else {
	  alert('Geolocation is not available. Using default location of Champaign, IL.');
	  fillFormWithCoordinates(DEFAULT_USER_LOCATION['lat'],
		    DEFAULT_USER_LOCATION['lng']);
	}
}

/**
* Initialize the modal dialog which indicates that the user's geolocation
* is being fetched and open it initially. 
*/
function initAndOpenDialog() {
  $('#dialog').dialog({
    width: 275,
    height: 60,
    autoOpen: true,
    modal: true,
  });		
}

/**
* Fill the form with the coordinates of the user location.
*/
function fillFormWithCoordinates(lat, lng) {
  $('#current_lat').val(lat);
  $('#current_lng').val(lng);
}

window.onload = getLocation;