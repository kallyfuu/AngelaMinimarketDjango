function iniciarMap(){
    var coord = {lat:-41.4661009 ,lng: -72.9885677};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 14,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}