document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Empêche la soumission par défaut du formulaire

        const searchInput = document.getElementById('search-input').value;
        const url = `http://localhost:5000/api/search?search=${encodeURIComponent(searchInput)}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erreur lors de la recherche');
                }
                return response.json();
            })
            .then(data => {
                data.forEach(function(film) {
                    // Création de l'élément <div> pour le nouveau film
                    var div = document.createElement("div");
                    div.classList.add("movie", "popup-trigger");
                    div.setAttribute('data-info', JSON.stringify({
                        "title": film.titre,
                        "year": "", // Vous pouvez ajouter l'année si disponible
                        "duration": "", // Ajoutez la durée du film si nécessaire
                        "rating": "", // Ajoutez la notation du film si nécessaire
                        "description": film.description,
                        "actors": film.nom + " " + film.prenom, // Format des acteurs
                        "director": "", // Ajoutez le réalisateur si nécessaire
                        "video": film.video
                    }));
                
                    // Ajout de l'image à l'intérieur du <div>
                    var img = document.createElement("img");
                    img.src = "static/images/" + film.image;
                    img.alt = film.titre;
                    div.appendChild(img);
                
                    // Ajout de l'étiquette "Ajout récent" sous forme de <div> avec la classe "label"
                    var label = document.createElement("div");
                    label.classList.add("label");
                    label.textContent = "Ajout récent";
                    div.appendChild(label);
                
                    // Ajout du titre du film en tant que paragraphe <p>
                    var p = document.createElement("p");
                    p.textContent = film.titre;
                    div.appendChild(p);
                
                    // Ajout du nouvel élément de film à la classe "movie-grid"
                    document.getElementsByClassName("movie-grid")[0].appendChild(div);
                });
            })
            .catch(error => {
                console.error('Erreur :', error);
            });
    });
});
