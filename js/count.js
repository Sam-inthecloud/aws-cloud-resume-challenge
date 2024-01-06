// update-visitor-count.js
const apiUrl = 'https://fq3sfkxl20.execute-api.eu-west-2.amazonaws.com/prod/UpdateVisitorCount';

async function updateVisitorCount() {
    try {
        console.log('Fetching visitor count...'); // Debugging: Log a message

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({}), // You can send an empty JSON object
        });

        if (response.status === 200) {
            console.log('API request successful.'); // Debugging: Log a message

            const data = await response.json();
            const visitorCount = data.visitorCount; // Assuming the response JSON structure has a 'VisitorCount' field
            
            // Debugging: Log the visitor count
            console.log('Visitor Count:', visitorCount);

            // Update the visitor count on your webpage
            const visitorCountElement = document.getElementById('visitor-count');
            if (visitorCountElement) {
                visitorCountElement.innerHTML = visitorCount;
                console.log('Visitor count updated on the webpage.'); // Debugging: Log a message
            } else {
                console.error('Element with ID "visitor-count" not found.'); // Debugging: Log an error
            }
        } else {
            console.error('API Error:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the function to update the visitor count when the page loads
window.onload = updateVisitorCount;
