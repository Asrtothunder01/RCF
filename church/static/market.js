// Smooth scroll for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Dynamic welcome message
const header = document.querySelector('header h1');
const welcomeMessages = [
    "Welcome to the Church Store!",
    "Your journey of faith starts here.",
    "Explore and uplift your spirit."
];
let messageIndex = 0;

setInterval(() => {
    header.textContent = welcomeMessages[messageIndex];
    messageIndex = (messageIndex + 1) % welcomeMessages.length;
}, 3000);

// Add animations to cards on scroll
const observer = new IntersectionObserver(
    entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-card');
            }
        });
    },
    { threshold: 0.1 }
);

document.querySelectorAll('.card').forEach(card => observer.observe(card));

// Validate contact form (if a form exists on the contact page)
if (window.location.pathname.includes('contact.html')) {
    const form = document.querySelector('form');
    form?.addEventListener('submit', function (e) {
        const name = document.querySelector('#name').value.trim();
        const email = document.querySelector('#email').value.trim();
        const message = document.querySelector('#message').value.trim();
        const errorDiv = document.querySelector('.error');

        if (!name || !email || !message) {
            e.preventDefault();
            errorDiv.textContent = "All fields are required.";
            errorDiv.style.display = "block";
        } else {
            errorDiv.style.display = "none";
            alert('Thank you for contacting us!');
        }
    });
}

// Add mobile-friendly menu toggle
const navbar = document.querySelector('.navbar');
const toggleButton = document.createElement('button');
toggleButton.classList.add('navbar-toggler');
toggleButton.setAttribute('data-bs-toggle', 'collapse');
toggleButton.setAttribute('data-bs-target', '#navbarNav');
toggleButton.innerHTML = '<span class="navbar-toggler-icon"></span>';
navbar.prepend(toggleButton);

// Dark mode toggle
const footer = document.querySelector('footer');
const darkModeButton = document.createElement('button');
darkModeButton.textContent = "Toggle Dark Mode";
darkModeButton.classList.add('btn', 'btn-secondary', 'mt-3');
footer.appendChild(darkModeButton);

darkModeButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// CSS for Dark Mode
const darkModeStyles = document.createElement('style');
darkModeStyles.textContent = `
    .dark-mode {
        background-color: #121212;
        color: #ffffff;
    }
    .dark-mode .card {
        background-color: #1e1e1e;
        border-color: #333;
    }
    .dark-mode .navbar, .dark-mode footer {
        background-color: #333;
    }
`;
document.head.appendChild(darkModeStyles);
