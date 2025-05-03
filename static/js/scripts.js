// JavaScript for edt2.html
// Get the button and file input elements
const uploadImageButton = document.getElementById('uploadImageButton');
const fileInput = document.getElementById('fileInput');

// Add click event listener to the button
uploadImageButton.addEventListener('click', () => {
    fileInput.click(); // Trigger the file input click
});

 // JavaScript for set location.html

// Initialize the map
var map = L.map('map').setView([17.2544, 78.3075], 13);

// Add a tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Example issues data
var issues = [
    [17.3850, 78.4867, "Waste (Garbage) Issue"],
    [17.3950, 78.4967, "Pothole Issue"],
    [17.4050, 78.5067, "Electric Issue"],
    [17.2544, 78.3075 , "Electric Issues"],
    [17.4150, 78.5167, "Waste (Garbage) Issue"],
    [17.4250, 78.5267, "Pothole Issue"],
    [17.4350, 78.5367, "Drainage Issue"],
    [17.4450, 78.5467, "Other Issue"]
];

// Add markers for each issue
issues.forEach(function(issue) {
            L.marker([issue[0], issue[1]]).addTo(map) 

            .bindPopup(issue[2]); 

});
