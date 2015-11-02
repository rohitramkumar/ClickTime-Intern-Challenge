from flask import Flask, render_template
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

from form import PrefsForm
from route import getDirections

# WSGI callable
app = Flask(__name__)

# Bootstrap extension
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  form = PrefsForm(csrf_enabled=False)
  if form.validate_on_submit():
    current_location = {
        'lat' : form.current_lat.data, 
        'lng' : form.current_lng.data }
    directions = getDirections(
        current_location, 
        form.transportation_mode.data,
        form.shop_preference.data)
    return render_template('results.html', directions=directions)
  return render_template('index.html', form=form)

if __name__ == '__main__':
  # For debugging purposes
  app.run(debug=True)

