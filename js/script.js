function getTimetable() {
    var rollNumber = document.getElementById("rollNumber").value.toUpperCase();
    
    // Convert roll number to integer for comparison
    var rollNum = parseInt(rollNumber);
    
    // Validate roll number range
    if (rollNum >= 25110001 && rollNum <= 25110361) {
        // Assuming the images are in the "img" folder
        var imageUrl = "img/" + rollNumber + ".png";
        
        // Redirect to the timetable image
        window.location.href = imageUrl;
    } else {
        alert("Invalid Roll Number! Please enter a roll number between 25110001 and 25110361.");
    }
}

