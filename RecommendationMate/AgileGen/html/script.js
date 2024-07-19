
document.addEventListener('DOMContentLoaded', () => {
    const userName = "John Doe"; // Example user name
    document.getElementById('user-name').textContent = userName;

    const savePreferencesButton = document.getElementById('save-preferences');
    const saveDislikedGenresButton = document.getElementById('save-disliked-genres');
    const refreshRecommendationsButton = document.getElementById('refresh-recommendations');

    savePreferencesButton.addEventListener('click', savePreferences);
    saveDislikedGenresButton.addEventListener('click', saveDislikedGenres);
    refreshRecommendationsButton.addEventListener('click', refreshRecommendations);

    function savePreferences() {
        const selectedGenres = Array.from(document.querySelectorAll('.user-preferences .genre-list input:checked')).map(input => input.value);
        console.log('Saved Preferences:', selectedGenres);
        // Implement saving preferences to backend or local storage
    }

    function saveDislikedGenres() {
        const dislikedGenres = Array.from(document.querySelectorAll('.disliked-genres .genre-list input:checked')).map(input => input.value);
        console.log('Saved Disliked Genres:', dislikedGenres);
        // Implement saving disliked genres to backend or local storage
    }

    function refreshRecommendations() {
        // Implement fetching new recommendations based on preferences and history
        const recommendations = [
            { title: 'Inception', genre: 'Sci-Fi', rating: 8.8, description: 'A thief who steals corporate secrets through the use of dream-sharing technology.' },
            { title: 'The Dark Knight', genre: 'Action', rating: 9.0, description: 'When the menace known as the Joker emerges from his mysterious past.' }
        ];
        displayRecommendations(recommendations);
    }

    function displayRecommendations(recommendations) {
        const recommendationList = document.getElementById('recommendation-list');
        recommendationList.innerHTML = '';
        recommendations.forEach(movie => {
            const movieCard = document.createElement('div');
            movieCard.className = 'movie-card';
            movieCard.innerHTML = `
                <h3>${movie.title}</h3>
                <p>Genre: ${movie.genre}</p>
                <p>Rating: ${movie.rating}</p>
                <p>${movie.description}</p>
                <button class="rate-movie">Rate Movie</button>
            `;
            recommendationList.appendChild(movieCard);
        });
    }

    // Initial load of recommendations
    refreshRecommendations();
});
