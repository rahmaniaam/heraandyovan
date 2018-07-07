function initMap() {
    const bidakara = {
        lat: -6.2401104,
        lng: 106.8408638
    }
    const map = new google.maps.Map(document.getElementById('map'), { zoom: 17, center: bidakara });
    const marker = new google.maps.Marker({ position: bidakara, map: map, animation: google.maps.Animation.BOUNCE });
}