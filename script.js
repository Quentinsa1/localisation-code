// Sélection des éléments du dessin SVG
const paths = document.querySelectorAll('.drawing path, .drawing circle, .drawing rect');
const hand = document.getElementById('hand');

let currentPath = 0;

// Fonction pour animer la main le long du dessin
function animateHand() {
    if (currentPath < paths.length) {
        const path = paths[currentPath];
        const length = path.getTotalLength();
        path.style.strokeDasharray = length;
        path.style.strokeDashoffset = length;

        let progress = 0;

        // Fonction de dessin progressif du tracé
        function draw() {
            progress += 2;
            if (progress <= length) {
                path.style.strokeDashoffset = length - progress;

                // Suivi de la position de la main
                const point = path.getPointAtLength(progress);
                hand.style.transform = `translate(${point.x}px, ${point.y}px)`;

                requestAnimationFrame(draw);
            } else {
                currentPath++;
                animateHand(); // Dessin du prochain élément
            }
        }
        draw();
    }
}

animateHand();


