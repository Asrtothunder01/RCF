document.addEventListener("DOMContentLoaded", () => {
  const welcomeText = "Welcome Aboard!";
  const welcomeHeading = document.querySelector(".display-4");
  const homeButton = document.querySelector(".btn-primary");

  // Typewriter Effect
  let charIndex = 0;
  const typeWriter = () => {
    if (charIndex < welcomeText.length) {
      welcomeHeading.textContent += welcomeText.charAt(charIndex);
      charIndex++;
      setTimeout(typeWriter, 100); // Adjust speed
    }
  };
  // Start typing
  welcomeHeading.textContent = "";
  typeWriter();

  // Add hover pulsating effect to the button
  homeButton.addEventListener("mouseenter", () => {
    homeButton.style.boxShadow = "0 0 20px 5px rgba(0, 123, 255, 0.7)";
    homeButton.style.transform = "scale(1.1)";
    homeButton.style.transition = "transform 0.3s, box-shadow 0.3s";
  });

  homeButton.addEventListener("mouseleave", () => {
    homeButton.style.boxShadow = "none";
    homeButton.style.transform = "scale(1)";
  });

  // Add confetti animation when the button is clicked
  homeButton.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent immediate navigation

    // Create confetti
    const confettiContainer = document.createElement("div");
    confettiContainer.style.position = "fixed";
    confettiContainer.style.top = "0";
    confettiContainer.style.left = "0";
    confettiContainer.style.width = "100%";
    confettiContainer.style.height = "100%";
    confettiContainer.style.pointerEvents = "none";
    confettiContainer.style.zIndex = "9999";

    document.body.appendChild(confettiContainer);

    for (let i = 0; i < 150; i++) {
      const confetti = document.createElement("div");
      confetti.style.position = "absolute";
      confetti.style.width = "10px";
      confetti.style.height = "10px";
      confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
      confetti.style.top = `${Math.random() * 100}%`;
      confetti.style.left = `${Math.random() * 100}%`;
      confetti.style.opacity = Math.random();
      confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
      confetti.style.animation = `fall ${Math.random() * 2 + 1}s ease-out`;

      confettiContainer.appendChild(confetti);

      confetti.addEventListener("animationend", () => {
        confetti.remove();
      });
    }

    // Navigate to the home page after animation
    setTimeout(() => {
      window.location.href = homeButton.getAttribute("href");
    }, 2000);
  });

  // Confetti fall animation
  const style = document.createElement("style");
  style.innerHTML = `
    @keyframes fall {
      0% {
        transform: translateY(-100vh);
      }
      100% {
        transform: translateY(100vh);
      }
    }
  `;
  document.head.appendChild(style);
});￼Enter
