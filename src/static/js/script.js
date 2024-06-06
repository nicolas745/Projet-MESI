// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('popup');
    const popupImage = popup.querySelector('.popup-image');
    const popupTitle = popup.querySelector('#popup-title');
    const popupYear = popup.querySelector('#popup-year');
    const popupDuration = popup.querySelector('#popup-duration');
    const popupRating = popup.querySelector('#popup-rating');
    const popupDescription = popup.querySelector('#popup-description');
    const popupActors = popup.querySelector('#popup-actors');
    const popupDirector = popup.querySelector('#popup-director');
    const closeBtn = popup.querySelector('.close');
    const popupTriggers = document.querySelectorAll('.popup-trigger');
    const videoPopup = document.getElementById('videoPopup');
    const videoPopupContent = document.querySelector('.video-popup-content');
    const videoClose = document.querySelector('.video-close');

    // Carousel functionality
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        const leftArrow = carousel.querySelector('.left-arrow');
        const rightArrow = carousel.querySelector('.right-arrow');
        const movieContainer = carousel.querySelectorAll('.movie');
        const totalMovies = movieContainer.length;
        let currentIndex = 0;

        function updateCarousel() {
            const offset = -currentIndex * (movieContainer[0].offsetWidth + 20); // 20 is the margin value, adjust if needed
            movieContainer.forEach(movie => {
                movie.style.transform = `translateX(${offset}px)`;
            });
        }

        leftArrow.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        });

        rightArrow.addEventListener('click', () => {
            if (currentIndex < totalMovies - 1) {
                currentIndex++;
                updateCarousel();
            }
        });
    });

    // Open film info popup
    function openPopup(data) {
        popupImage.src = data.image;
        popupTitle.textContent = data.title;
        popupYear.textContent = `Year: ${data.year}`;
        popupDuration.textContent = `Duration: ${data.duration}`;
        popupRating.textContent = `Rating: ${data.rating}`;
        popupDescription.textContent = data.description;
        popupActors.textContent = `Actors: ${data.actors}`;
        popupDirector.textContent = `Director: ${data.director}`;
        popup.style.display = 'block';

        // Attach event listener to the watch button
        const watchButton = document.querySelector('.popup-button.watch');
        watchButton.addEventListener('click', () => {
            popup.style.display = 'none';
            videoPopup.style.display = 'block';
        });
    }

    // Close film info popup
    closeBtn.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    // Close film info popup by clicking outside
    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });

    // Open film info popup on trigger click
    popupTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const data = JSON.parse(trigger.getAttribute('data-info'));
            data.image = trigger.querySelector('img').src; // Get the image source from the trigger element
            openPopup(data);
        });
    });

    document.getElementById('search-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const searchInput = document.getElementById('search-input').value;
        
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ search: searchInput })
        })
        .then(response => response.json())
        .then(data => {
            const movieGrid = document.querySelector('.movie-grid');
            movieGrid.innerHTML = ''; // Clear previous results
            data.forEach(movie => {
                const movieElement = document.createElement('div');
                movieElement.className = 'movie';
                movieElement.innerHTML = `
                    <h3>${movie.titre}</h3>
                    <p>${movie.nom} ${movie.prenom}</p>
                    <p>${movie.annee}</p>
                    <p>${movie.duree}</p>
                    <p>${movie.note}</p>
                    <p>${movie.description}</p>
                `;
                movieGrid.appendChild(movieElement);
            });
        })
        .catch(error => console.error('Error:', error));
    });    
});
