from wtforms import SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import Form

class PrefsForm(Form):
  """Defines a form that retrieves some preferences as to how the user 
  wants to generate the route and what donut shop they want."""

  current_lat = FloatField('Current latitude:', validators=[DataRequired()])
  current_lng = FloatField('Current longitude:', validators=[DataRequired()])
  transportation_mode = SelectField(
      'Mode of transportation:', 
      choices=[('driving', 'Driving'), ('bicycling', 'Bicycling'), 
      ('transit', 'Public Transit/Walking')], default='transit')
  shop_preference = SelectField(
      'Donut Shop Preference:', 
      choices=[('distance', 'Distance'), ('prominence', 'Prominence')], 
      default='distance')

  submit = SubmitField('Submit')