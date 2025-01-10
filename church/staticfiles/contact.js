// futuristic.js

// Onload animation for the header
document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");
    header.style.transition = "all 1.5s ease";
    header.style.transform = "scale(1.2)";
    header.style.opacity = "0";
    setTimeout(() => {
        header.style.transform = "scale(1)";
        header.style.opacity = "1";
    }, 200);
});

// Real-time validation with glowing effects
const inputs = document.querySelectorAll("input, textarea");
inputs.forEach(input => {
    input.addEventListener("input", () => {
        if (input.value.trim()) {
            input.style.border = "2px solid limegreen";
            input.style.boxShadow = "0 0 10px limegreen";
        } else {
            input.style.border = "2px solid red";
            input.style.boxShadow = "0 0 10px red";
        }
    });
});

// Submit form interaction
const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if (name && email && message) {
        alert(`
            Name: ${name}
            Email: ${email}
            Message: ${message}

            We have received your message. Thank you!
        `);
        form.reset();
        // Reset glowing effects
        inputs.forEach(input => {
            input.style.border = "";
            input.style.boxShadow = "";
        });
    } else {
        alert("Please fill out all fields before submitting.");
    }
});

// Dynamic background for the main section
const main = document.querySelector("main");
main.style.transition = "background 0.5s ease";
setInterval(() => {
    const colors = ["#f3e5f5", "#e8f5e9", "#e3f2fd", "#fff3e0"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    main.style.background = randomColor;
}, 2000);

// Navbar glow on hover
const navLinks = document.querySelectorAll(".nav-link");
navLinks.forEach(link => {
    link.addEventListener("mouseover", () => {
        link.style.transition = "all 0.3s ease";
        link.style.textShadow = "0 0 8px cyan";
        link.style.color = "cyan";
    });
    link.addEventListener("mouseout", () => {
        link.style.textShadow = "";
        link.style.color = "";
    });
});

// Footer hover animation
const footer = document.querySelector("footer");
footer.addEventListener("mouseover", () => {
    footer.style.transition = "all 0.3s ease";
    footer.style.background = "linear-gradient(90deg, #ff8a80, #ff80ab, #ea80fc)";
    footer.style.color = "#000";
});
footer.addEventListener("mouseout", () => {
    footer.style.background = "black";
    footer.style.color = "white";
});￼Enter
