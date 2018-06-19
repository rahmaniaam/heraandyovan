function initMap() {
    const bidakara = {
        lat: -6.241699,
        lng: 106.841279
    }
    const map = new google.maps.Map(document.getElementById('map'), { zoom: 18, center: bidakara });
    const marker = new google.maps.Marker({ position: bidakara, map: map, animation: google.maps.Animation.BOUNCE });
}