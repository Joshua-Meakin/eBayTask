# Take home exercise

This is an interesting task, I have enjoyed it a lot :P

In this task, I completed RESTful service and webpage based on Python and Flask. For the basic service, I introduced another method to calculate the price(distance) between two postcodes. The details will be presented in each section. Apart from making a responsive page, I got all the other jobs done.

# Features completed

### Distance calculation

Personally, I think calculate the distance by latitude and longitude is a better idea. To implement it, I firstly used Postcodes.io to verify the input postcodes and convert them into a set of coordinations, then past the coordinations to GeoPy. GeoPy is a library for geocoding. In distance calculation, GeoPy uses a spherical model of the earth, which uses the mean earth radius as defined by the International Union of Geodesy and Geophysics.

The implementation of this part is all in app/service.py.

### Webpage interface for app

I used jinja2 to present webpage and Flask-WTF to pass data. All the fields in the webpage are set to be compulsory, otherwise the user cannot submit the form.

# Personal ideas

Consider large a mount of data and access, this may not be a good solution as it is very likely to cause waiting for the response from Postcode.io. I think the best way to deal with this application is to build a high accurate database for postcodes with its longtitude and latitude. For its best performance, those high frequent postcodes should be made into index.

# Dependencies

All the dependencies are recorded in requirements.txt, please install it with pip.
```
pip install -r requirements.txt
```

Start the server
```
python app/app.py
```
Note that the service runs at port 8080.