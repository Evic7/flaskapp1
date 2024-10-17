from datetime import datetime
from flask import Flask, render_template, url_for, request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from opencage.geocoder import OpenCageGeocode


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    """ if request.method == 'POST':
      number1 = request.form['pnumber']
      number2 = request.form['pnumber2']
      
      if number2 == "":
          return number1 + "<br>" "the second number is not given"
      else:
          return number1 +" "+ number2
       """
    return render_template("index.html")
  
@app.route('/locator/',methods=['GET','POST'])
def locator():
 try:
  # taking input the phonenumber along with the country code
  if request.method == 'POST':
      number1 = request.form['pnumber']
      outputs = {"phone1":number1}
      
      if "." in number1:
        try:
          res = DbIpCity.get(number1, api_key="free")
          print(f"IP Address: {res.ip_address}")
          outputs.update({"ipaddress": res.ip_address})
          print(f"Location: {res.city}, {res.region}, {res.country}")
          outputs.update({"iplocation": res.city+","+res.region+","+res.country })
          print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
          outputs.update({"ipcoord": f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})"})
          outputs.update({"lat1": res.latitude})
          outputs.update({"lng1": res.longitude})
        except Exception as e:
          print(e)
          outputs.update({"mainerror": "An error occured while getting ip details you can try again"})
        return render_template("locate.html",outputs = outputs)  
      # Parsing the phonenumber string to convert it into phonenumber format
      phoneNumber = phonenumbers.parse(number1)
      
      # Storing the API Key in the Key variable
      Key = "875749ed67fa42288d1e1ba4a255350c"
      #Key='3e2e0c0712504517a9e2bdfb4b29be29'   #backup key
 
      # Using the geocoder module of phonenumbers to print the Location in console
      yourLocation = geocoder.description_for_number(phoneNumber,"en")
      
      #print("location : "+yourLocation)
      outputs.update({"location": yourLocation})
      
 
      # Using the carrier module of phonenumbers to print the service provider name in console
      yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
      #print("service provider : "+yourServiceProvider)
      outputs.update({"serviceprovider": yourServiceProvider})
      
      # Using opencage to get the latitude and longitude of the location
      numgeocoder = OpenCageGeocode(Key)
      query = str(yourLocation)
      results = numgeocoder.geocode(query)
 
      # Assigning the latitude and longitude values to the lat and lng variables
      lat = results[0]['geometry']['lat']
      lng = results[0]['geometry']['lng']
      outputs.update({"lat1": lat})
      outputs.update({"lng1": lng})
      """  # Getting the map for the given latitude and longitude
      myMap = folium.Map(location=[lat,lng],zoom_start = 15)
      #Add a red circle marker to the map at the specified 'location' 
      folium.CircleMarker(location=[lat,lng], radius=50, color="red").add_to(myMap)

      #Add a standard marker (pin) to the map at the same 'location' coordinates
      folium.Marker(location=[lat,lng]).add_to(myMap)
      
      myMap.get_root().width = "800px"
      myMap.get_root().height = "600px"
      # get folium result in an html iframe tags
      mapfme = myMap.get_root()._repr_html_()
      
      outputs.update({"mapframe": mapfme})  """
 except Exception as e:
     error = "An error occured you can try again"
     print(e)
     outputs.update({"mainerror": error})
 print(outputs)

 return render_template("locate.html",outputs = outputs)
 
if __name__ == "__main__":
    app.run(debug=True)