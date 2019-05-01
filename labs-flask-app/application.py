import datetime
from decouple import config
from flask import Flask, request
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests

# Create and configure an instance of the Flask application.
application = app = Flask(__name__)
FlaskJSON(app)
CORS(app)

# Initialize environment variables
token = os.environ['AZAVEA_API_TOKEN']
baseurl = 'https://app.climate.azavea.com'
header = {'Authorization': 'Token {}'.format(token)}

# Wrapper function to fetch indicator information based on lat and long
# from Azavea Climate API
def get_indicator_by_latlong(lat, lon, indicator_name):
    """
    Wrapper function to fetch indicator information based on lat and long
    from Azavea Climate API.
    """
    endpoint=f'/api/climate-data/{lat}/{lon}/RCP45/indicator/{indicator_name}/'
    
    # Custom year setting
    now = datetime.datetime.now()
    year_range = str(now.year)+':'+str(2100)
    
    optional_parameters=f'?agg=max,avg&years={year_range}'
    
    url = baseurl+endpoint+optional_parameters
    
    # Trigger the request
    response = requests.get(url, headers=header)
    
    return response.ok, response.json()

@app.route('/prediction', methods=['POST'])
def get_prediction():
    """
    Get predictions based on latitude and longitude of a given location.
    The predictions are fetched using Azavea Climate API.

    NEX-GDDP dataset and climate model RCP4.5 is being used for prediction.

    Input: 
        latitude and longitude of location of interest.

    Output:
        Count of extreme climate incidents from present year till 2100.
        1. Dry Spells.
        2. Extreme Cold Events.
        3. Extreme Heat Events.
        4. Extreme Precipitation Events.
        5. Heat Wave Incidents.
    """

    data = request.get_json(force=True)
    try:
        latitude = data['latitude']
        longitude = data['longitude']
    except (KeyError):
        raise JsonError(description='Key Error: Key missing in the request')

    # Invoke Azavea Climate API
    result = {'dry_spells' : "",
            'extreme_cold_events': "",
            'extreme_heat_events': "",
            'extreme_precipitation_events': "",
            'heat_wave_incidents': ""}
    
    for key in result.keys():
        ok, response = get_indicator_by_latlong(latitude, longitude, key)
        
        if ok:
            result[key]=response['data']
        else:
            result[key]=response['detail']

    return json_response(latitude=latitude,
            longitude=longitude,
            prediction=result)


@app.route('/')
def root():
    """
    Testing elastic bean
    """
    return "Test Successful"

if __name__ == '__main__':
    application.run(debug=True)
