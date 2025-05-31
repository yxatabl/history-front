document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    const map = L.map('map').setView([64.5, 26.0], 6);
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // DOM elements
    const eventsContainer = document.getElementById('events-container');
    const eventsList = document.getElementById('events-list');
    const eventDetails = document.getElementById('event-details');
    const markdownContent = document.getElementById('markdown-content');
    const backButton = document.getElementById('back-button');
    
    // Markers array to keep track of map markers
    let markers = [];
    
    // Fetch events from Flask API
    fetchEvents();
    
    // Function to fetch events
    function fetchEvents() {
        eventsContainer.innerHTML = '<div class="loader"></div>';
        
        fetch('/api/events')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(events => {
                displayEvents(events);
                addMarkersToMap(events);
            })
            .catch(error => {
                console.error('Error fetching events:', error);
                eventsContainer.innerHTML = '<p>Error loading events. Please try again later.</p>';
            });
    }
    
    // Function to display events in the info panel
    function displayEvents(events) {
        eventsContainer.innerHTML = '';
        
        if (events.length === 0) {
            eventsContainer.innerHTML = '<p>No events found.</p>';
            return;
        }
        
        events.forEach(event => {
            const eventCard = document.createElement('div');
            eventCard.className = 'event-card';
            eventCard.dataset.id = event.id;
            
            eventCard.innerHTML = `
                <h3>${event.title}</h3>
                <p><strong>Расположение:</strong> ${event.place.name}</p>
            `;
            
            eventCard.addEventListener('click', () => showEventDetails(event));
            eventsContainer.appendChild(eventCard);
        });
    }
    
    // Function to add markers to the map
    function addMarkersToMap(events) {
        // Clear existing markers
        markers.forEach(marker => map.removeLayer(marker));
        markers = [];
        
        events.forEach(event => {
            const marker = L.marker([event.place.latitude, event.place.longitude])
                .addTo(map)
                .bindPopup(`<b>${event.title}</b><br>${event.place.name}`);
            
            marker.on('click', () => showEventDetails(event));
            markers.push(marker);
        });
    }
    
    // Function to show event details
    function showEventDetails(event) {
        // Hide events list and show details
        eventsList.style.display = 'none';
        eventDetails.style.display = 'block';
        
        // Render markdown content
        markdownContent.innerHTML = marked.parse(event.markdown);
        
        // Highlight the corresponding marker
        markers.forEach(marker => {
            const latLng = marker.getLatLng();
            if (latLng.lat === event.place.latitude && latLng.lng === event.place.longitude) {
                marker.openPopup();
                map.setView([event.place.latitude, event.place.longitude], 8);
            }
        });
    }
    
    // Back button event listener
    backButton.addEventListener('click', () => {
        eventDetails.style.display = 'none';
        eventsList.style.display = 'block';
    });
});