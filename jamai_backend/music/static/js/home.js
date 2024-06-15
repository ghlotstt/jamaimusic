document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.section').forEach(section => {
        section.addEventListener('mouseover', () => {
            const h2 = section.querySelector('h2');
            const p = section.querySelector('p');

            // Reset text content to trigger animation
            h2.style.width = '0';
            p.style.width = '0';
            h2.style.animation = 'none';
            p.style.animation = 'none';
            setTimeout(() => {
                h2.style.animation = 'typing 2s steps(20, end) forwards, blink 0.75s step-end infinite';
                p.style.animation = 'typing 3s steps(40, end) forwards, blink 0.75s step-end infinite';
                h2.style.width = '';
                p.style.width = '';
            }, 10);
        });
    });
});
