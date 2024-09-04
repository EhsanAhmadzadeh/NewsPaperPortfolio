document.addEventListener('DOMContentLoaded', function () {
    // Example: Highlight the card on hover
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseover', function () {
            this.classList.add('shadow-lg');
        });
        card.addEventListener('mouseout', function () {
            this.classList.remove('shadow-lg');
        });
    });
});
