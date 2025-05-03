function initMap() {
    // Initialize the map
    var map = L.map('map').setView([17.2544, 78.3075], 13);

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    // Add a marker in the center
    var marker = L.marker([17.2544, 78.3075]).addTo(map)
        .bindPopup('Current Location')
        .openPopup();

    // Add a marker on click
    map.on('click', function(e) {
        marker.setLatLng(e.latlng);
        document.getElementById('selectedLocation').value = e.latlng.lat + ',' + e.latlng.lng; // Store the coordinates
    });

    // Set location button
    document.getElementById('setLocationButton').addEventListener('click', function() {
        if (marker) {
            window.location.href = 'setcomplain.html?location=' + document.getElementById('selectedLocation').value;
        } else {
            alert('Please select a location on the map.');
        }
    });
}
