function createMatrixEffect() {
    const background = document.getElementById('matrixBackground');
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789αβγδεζηθικλμνξοπρστυφχψω';
    const columns = Math.floor(window.innerWidth / 20);

    function createCharacter() {
        const span = document.createElement('span');
        span.className = 'matrix-character';
        span.textContent = characters[Math.floor(Math.random() * characters.length)];
        span.style.left = `${Math.floor(Math.random() * columns) * 20}px`;
        span.style.animationDuration = `${Math.random() * 2 + 3}s`;
        span.style.opacity = Math.random() * 0.5 + 0.5;
        
        span.addEventListener('animationend', () => {
            span.remove();
            createCharacter();
        });
        
        background.appendChild(span);
    }

    for (let i = 0; i < columns; i++) {
        setTimeout(() => {
            createCharacter();
        }, Math.random() * 5000);
    }
}

createMatrixEffect();

window.addEventListener('resize', () => {
    const background = document.getElementById('matrixBackground');
    background.innerHTML = '';
    createMatrixEffect();
});