document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = "Welcome Aboard!";
  const welcomeHeading = document.querySelector(".display-4");
  const homeButton = document.querySelector(".btn-primary");

  // Typewriter Effect
  let charIndex = 0;
  function typeWriter() {
    if (charIndex < welcomeText.length) {
      welcomeHeading.textContent += welcomeText.charAt(charIndex);
      charIndex++;
      setTimeout(typeWriter, 100); // Adjust speed
    }
  }
  // Start typing
  welcomeHeading.textContent = "";
  typeWriter();

  // Add hover pulsating effect to the button using CSS class
  homeButton.classList.add("hover-effect");

  // Add confetti animation when the button is clicked
  homeButton.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent immediate navigation

    // Create confetti
    const confettiContainer = document.createElement("div");
    confettiContainer.classList.add("confetti-container");
    document.body.appendChild(confettiContainer);

    for (let i = 0; i < 150; i++) {
      const confetti = document.createElement("div");
      confetti.classList.add("confetti");
      confettiContainer.appendChild(confetti);

      confetti.addEventListener("animationend", function () {
        confetti.remove();
      });
    }

    // Navigate to the home page after animation
    setTimeout(function () {
      window.location.href = homeButton.getAttribute("href");
    }, 2000);
  });
});
