from flask import Flask, render_template

from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form

from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

import route

"""Defines a form that retrieves some preferences as to how the user
wants to generate the route and what donut shop they want.
TODO: Should this be in a seperate module?"""
class PrefsForm(Form):
  current_lat = StringField(
      'Current latitude: ( You can edit this field if want )')
  current_lng = StringField(
      'Current longitude: ( You can edit this field if want )')
  transportation_mode = RadioField('Mode of transportation:', 
      choices=[('driving', 'Driving'), ('bicycling', 'Bicycling'), 
      ('transit', 'Public Transit/Walking')], default='driving')
  shop_preference = RadioField('Donut Shop Preference:', 
      choices=[('distance', 'Distance'), ('prominence', 'Prominence')], 
      default='distance')

  submit = SubmitField('Submit')

# WSGI callable
app = Flask(__name__)

# Bootstrap extension
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  form = PrefsForm(csrf_enabled=False)
  if form.validate_on_submit():
    current_location = {
        'lat' : float(form.current_lat.data), 
        'lng' : float(form.current_lng.data) }
    directions = route.getDirections(current_location, 
        form.transportation_mode.data,
        form.shop_preference.data)
    return render_template('results.html', directions=directions)
  return render_template('index.html', form=form)

if __name__ == '__main__':
  # For debugging purposes
  app.run(debug=True)

