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
    const movieGrid = document.querySelector('.recommended .movie-grid');
    const leftArrow = document.querySelector('.recommended .left-arrow');
    const rightArrow = document.querySelector('.recommended .right-arrow');


    leftArrow.addEventListener('click', () => {
        movieGrid.scrollBy({
            left: -movieGrid.clientWidth,
            behavior: 'smooth'
        });
    });


    rightArrow.addEventListener('click', () => {
        movieGrid.scrollBy({
            left: movieGrid.clientWidth,
            behavior: 'smooth'
        });
    });


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
    }


    closeBtn.addEventListener('click', () => {
        popup.style.display = 'none';
    });


    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });


    popupTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const data = JSON.parse(trigger.getAttribute('data-info'));
            data.image = trigger.querySelector('img').src; // Get the image source from the trigger element
            openPopup(data);
        });
    });
});



