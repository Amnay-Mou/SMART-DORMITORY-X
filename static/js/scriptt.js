// Select the background container
const backgroundContainer = document.querySelector('.background-container');

// Add event listener to track mouse movement
document.addEventListener('mousemove', (e) => {
    // Calculate the percentage of movement based on cursor position
    const moveX = (e.clientX / window.innerWidth - 0.5) * 100;
    const moveY = (e.clientY / window.innerHeight - 0.5) * 100;

    // Apply parallax effect to the background container
    gsap.to(backgroundContainer, {
        duration: 1,
        x: moveX,
        y: moveY,
        ease: 'power2.out' // Adjust easing as needed
    });
});



