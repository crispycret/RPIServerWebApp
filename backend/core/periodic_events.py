""" 
This moudle should provide functionality for time based events.
Such as, retrieving data from the live plant API to store in the database. 
"""
from requests import request


from apscheduler.triggers.interval import IntervalTrigger


def fetch_live_data():
    """ 
    Make a request to the plant data api endpoint to retrive the plant data.
    Make a post request to save the plant data to the database on this endpoint.
    """
    # Read plant endpoint from the .env file to secure the server location.
    # Provide access token in env? or use jwt upon authentication?
    # If using jwt, must use here as wll.
    plant_endpoint = 'https://plantwaterer.ngrok.io/v1/data'
    db_endpoint = 'http://localhost:5000/save'

    # Will be needed when authentication is required.
    payload={}
    headers={}

    # Get plant data from live api endpoint
    response = request("GET", plant_endpoint, headers=headers, data=payload)
    
    # Expect no other response status than 200
    # Request to the live data api failed, handle the error.
    # Change time interval of fetching data until response status is 200. 
    if response.status_code != 200:
        # No need to request the data every minute if the live data api is down.
        return

    # If the request was successful, make a request to store data in database.
    # Set authorization header if implemented.
    headers['Authorization'] = 'place token here'
    response = request('POST',db_endpoint, headers={}, json=response.json()['data'])
    
    # Handle failed request [Log Error, adjust job interval]
    if (response.status_code != 200): pass
    return    

