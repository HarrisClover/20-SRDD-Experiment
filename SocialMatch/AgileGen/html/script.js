
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Simulate sending confirmation email
    alert('A confirmation email has been sent to your email address.');
    
    // Redirect to profile completion page
    window.location.href = 'profile-completion.html';
});
