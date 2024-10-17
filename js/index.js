var forms = document.getElementById("forms")
var field2 = document.getElementById("pn2")
var vsn = document.getElementById("viewsndnum")



//location
var latde = ""
var lngtde = ""  
function getLocation() {
if (navigator.geolocation) {
navigator.geolocation.watchPosition(showPosition, showError);
} else { 
responses("Update your browser.");
}
}

function showPosition(position) {
var mframe = document.getElementById("mapframe")
latde=position.coords.latitude
lngtde=position.coords.longitude

//responses("Latitude: " + position.coords.latitude + 
//"<br>Longitude: " + position.coords.longitude)

mframe.src="https://maps.google.com/maps?q="+position.coords.latitude+","+position.coords.longitude+"&amp;z=15&amp;&output=embed" 

}

function showError(error) {
switch(error.code) {
case error.PERMISSION_DENIED:
responses("User denied the request for Geolocation.")
break;
case error.POSITION_UNAVAILABLE:
responses("Location information is unavailable.")
break;
case error.TIMEOUT:
responses("Location request timed out.")
break;
case error.UNKNOWN_ERROR:
responses("Error Unknown.")
break;
}
}
function responses(resp){
var errh = document.getElementById("errorhandler")
errh.style.display="block"
errh.innerHTML= resp
}

// for hide location area
function  hidelocator(){
var h = document.getElementById("hidelocate")
loc = document.getElementById("locate")
let i = 0;
var si = setInterval(()=>{
  if(i == 100){
    clearInterval(si)
    loc.style.display="none"
    loc.style.top=0
    i=0
  }else{
    i+=10
    loc.style.top=i+"%"
  }

},50)

}
var number1 = document.getElementById("pn")
forms.onsubmit =(e)=>{
 e.preventDefault()
 
let num1 = document.forms["form1"]["pnumber"].value

if(num1==""){
 number1.style.border="2px solid red"
}else{
loadDoc()
}
function loadDoc() {
  document.getElementById("locate").style.display="block"
 
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    document.getElementById("locate").innerHTML = this.responseText;
    document.getElementById("send").innerHTML = " Get Location "
    internalmsg()
    }
  }
  xhttp.open("POST", "/locator/", true);
  const form = new FormData()
  form.append("pnumber",num1)
  xhttp.send(form);

 
  
}


} 
 function showdetails(){
  document.getElementById("fulldetail").style.display="block"
 }
 function closedetails(){
  document.getElementById("fulldetail").style.display="none"
 }
 function internalmsg(){
  var frame = document.getElementById("mapframe")
  var numlat = document.getElementById("lat")
  var numlng = document.getElementById("lng")
  var er = document.getElementById("internalerror")
  var map = document.getElementById("map")
  if (er.innerHTML != ""){
    responses(er.innerHTML)
  }else if (numlat.innerHTML == ""){
    responses("Phone number location is not available")

  }else if (numlng.innerHTML == ""){
    responses("Phone number location is not available")

  }else{

frame.src="https://maps.google.com/maps?q="+numlat.innerHTML+","+numlng.innerHTML+"&amp;z=15&amp;&output=embed" 

//responses(map.innerText)
}
}


