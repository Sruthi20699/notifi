document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('joinUsButton').addEventListener('click', function() {
        window.location.href = '/login'; // Redirect to the login page
    });
});

const we = new WebSocket('ws://127.0.0.1:8000/ws/notifications/')

ws.onmessage = function(event){
    const notificationData = JSON.parse(event.data)
    displayNotification(notificationData);
}

function displayNotification(notificationData){
    const notificationList = document.getElementById('notificationList')
    const { sender_id, recipient_id, message} = notificationData

    const notificationItem = document.createElement('li')
    notificationItem.textContent = 'From : ${sender_id} | Message : ${message}'
    notificationList.appendChild(notificationItem)
}