import datetime
from decouple import config
from flask import Flask, request
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response
import os
import psycopg2 as pg
import requests


# Create and configure an instance of the Flask application.
application = app = Flask(__name__)
FlaskJSON(app)
CORS(app)

# Initialize environment variables
token = os.environ['AZAVEA_API_TOKEN']
user = os.environ['DB_USER_NAME']
password = os.environ['DB_PASSWORD']

# Global variables
baseurl = 'https://app.climate.azavea.com'
header = {'Authorization': 'Token {}'.format(token)}
database = 'LiveSafeDB'
host = 'livesafe-lab12-project.cyplld0jesr7.us-east-1.rds.amazonaws.com'
port = '5432'


def get_indicator_by_latlong(lat, lon, indicator_name, years):
    """
    Wrapper function to fetch indicator information based on lat and long
    from Azavea Climate API.
    """

    endpoint = f'/api/climate-data/{lat}/{lon}'  # noqa: E999
    endpoint += f'/RCP45/indicator/{indicator_name}/'

    # Custom year setting
    now = datetime.datetime.now()
    final_year = min(now.year+years, 2100)
    year_range = str(now.year)+':'+str(final_year)

    # Maximum allowed distance (meters) to Map Cell from provided Lat + Lon
    distance = 30000.0

    # Select LOCA dataset
    dataset = 'LOCA'

    optional_parameters = f'?dataset={dataset}&distance={distance}'
    optional_parameters += f'&agg=max,avg&years={year_range}'

    url = baseurl+endpoint+optional_parameters

    # Trigger the request
    response = requests.get(url, headers=header)

    return response.ok, response.json()


@app.route('/allpredictions', methods=['POST'])
def get_all_predictions():
    """
    Get predictions based on latitude and longitude of a given location.
    The predictions are fetched using Azavea Climate API.

    LOCA dataset and climate model RCP4.5 is being used for prediction.

    Input:
        latitude and longitude of location of interest.
        years to specify the range of years for fetching the predictions.

    Output:
        Count of extreme climate incidents from present year till
        years range or 2100.
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
        years = data['years']
    except (KeyError):
        raise JsonError(description='Key Error: Key missing in the request')

    # Invoke Azavea Climate API
    result = {'dry_spells': "",
              'extreme_cold_events': "",
              'extreme_heat_events': "",
              'extreme_precipitation_events': "",
              'heat_wave_incidents': ""}

    for key in result.keys():
        ok, response = get_indicator_by_latlong(latitude, longitude,
                                                key, years)

        if ok:
            result[key] = response['data']
        else:
            result[key] = response['detail']

    return json_response(latitude=latitude,
                         longitude=longitude,
                         prediction=result)


@app.route('/prediction', methods=['POST'])
def get_prediction():
    """
    Get specific indicator prediction based on latitude and longitude
    of a given location. The prediction is fetched using Azavea Climate API.

    LOCA dataset and climate model RCP4.5 is being used for prediction.

    Input:
        latitude and longitude of location of interest.
        years to specify the range of years for fetching the prediction.
        indicator to specify the name of indicator of prediction.
        1. dry_spells - Dry Spells.
        2. extreme_cold_events - Extreme Cold Events.
        3. extreme_heat_events - Extreme Heat Events.
        4. extreme_precipitation_events - Extreme Precipitation Events.
        5. heat_wave_incidents - Heat Wave Incidents.

    Output:
        Count of extreme climate incidents from present year till
        years range or 2100.
    """

    data = request.get_json(force=True)
    try:
        latitude = data['latitude']
        longitude = data['longitude']
        years = data['years']
        indicator = data['indicator']
    except (KeyError):
        raise JsonError(description='Key Error: Key missing in the request')

    # Invoke Azavea Climate API
    result = {}

    ok, response = get_indicator_by_latlong(latitude, longitude,
                                            indicator, years)

    if ok:
        result[indicator] = response['data']
    else:
        result[indicator] = response['detail']

    return json_response(latitude=latitude,
                         longitude=longitude,
                         prediction=result)


@app.route('/history', methods=['POST'])
def get_history():
    """
    Get information on historical event count for a particular county.

    Input:
        fipscode specific to the county.
        startyear from which the events needs to be returned.
        endyear till which the events needs to be returned.
        For querying a specific year startyear = endyear

    Output:
        Aggregated count of weather events in a paricular county by year.
        1. Winter Weather.
        2. Storm.
        3. Flood.
        4. Fire.
        5. Heat.
        6. Drought.
        7. Tornado.
        8. Hurricane.
        9. Earthquake.
    """

    # Establish DB connection
    pg_conn = pg.connect(database=database, user=user, password=password,
                         host=host, port=port)

    data = request.get_json(force=True)
    try:
        fipscode = data['fipscode']
        startyear = data['startyear']
        endyear = data['endyear']
    except (KeyError):
        raise JsonError(description='Key Error: Key missing in the request')

    # Invoke DB query
    pg_cur = pg_conn.cursor()
    get_county_info = f"""SELECT * FROM noaa_historical
    WHERE fipscode={fipscode} AND year BETWEEN {startyear} AND {endyear};
    """
    pg_cur.execute(get_county_info)

    count = pg_cur.rowcount
    if count == 0:
        # Close the cursor
        pg_cur.close()

        return json_response(fipscode=fipscode,
                             startyear=startyear,
                             endyear=endyear,
                             count=count)

    # Populate result
    rows = pg_cur.fetchall()
    result = {}

    for row in rows:
        # Create yearwise records
        year_record = {}
        year_record['winterweather'] = row[2]
        year_record['storm'] = row[3]
        year_record['flood'] = row[4]
        year_record['fire'] = row[5]
        year_record['heat'] = row[6]
        year_record['drought'] = row[7]
        year_record['tornado'] = row[8]
        year_record['hurricane'] = row[9]
        year_record['earthquake'] = row[10]

        # Append to overall result by year
        result[row[0]] = year_record

    # Close the cursor
    pg_cur.close()

    return json_response(fipscode=fipscode,
                         startyear=startyear,
                         endyear=endyear,
                         count=count,
                         history=result)


@app.route('/')
def root():
    """
    Testing elastic bean
    """
    return "Test Successful"


if __name__ == '__main__':
    application.run()
