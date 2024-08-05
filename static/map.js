// static/map.js
document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map-container').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    // Ajouter des marqueurs dynamiquement ici
    // Example: L.marker([51.5, -0.09]).addTo(map);
});
