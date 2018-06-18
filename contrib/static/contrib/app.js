// Register device for push notifications
Pushy.register({ appId: '' }).then(function (deviceToken) {
    // Print device token to console
    console.log('Pushy device token: ' + deviceToken);

    // Send the token to your backend server via an HTTP GET request
    //fetch('https://your.api.hostname/register/device?token=' + deviceToken);

    // Succeeded, optionally do something to alert the user
}).catch(function (err) {
    // Handle registration errors
    console.error(err);
});