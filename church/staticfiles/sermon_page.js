// Add loading animation
document.addEventListener('DOMContentLoaded', () => {
    // Create and append loading element
    const loading = document.createElement('div');
    loading.className = 'loading';
    document.body.appendChild(loading);

    // Remove loading animation after content loads
    window.addEventListener('load', () => {
        loading.style.opacity = '0';
        setTimeout(() => loading.remove(), 500);
    });

    // Smooth scroll functionality
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Initialize audio player with custom controls
    const audio = document.querySelector('audio');
    if (audio) {
        // Add time update listener
        audio.addEventListener('timeupdate', () => {
            const progress = (audio.currentTime / audio.duration) * 100;
            // Update custom progress bar if you add one
        });

        // Add error handling
        audio.addEventListener('error', () => {
            console.error('Error loading audio file');
            // Show user-friendly error message
            const audioSection = document.querySelector('.audio-section');
            if (audioSection) {
                audioSection.innerHTML += '<p class="text-danger">Sorry, there was an error loading the audio. Please try again later.</p>';
            }
        });
    }

    // Add scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for scroll animations
    document.querySelectorAll('.sermon-details, .audio-section').forEach(el => {
        observer.observe(el);
    });

    // Add dynamic verse highlighting
    const memoryVerse = document.querySelector('.sermon-details p:first-child');
    if (memoryVerse) {
        memoryVerse.addEventListener('mouseenter', () => {
            memoryVerse.style.transform = 'scale(1.02)';
            memoryVerse.style.backgroundColor = '#f8f9fa';
        });

        memoryVerse.addEventListener('mouseleave', () => {
            memoryVerse.style.transform = 'scale(1)';
            memoryVerse.style.backgroundColor = 'transparent';
        });
    }

    // Add responsive navbar functionality
    const nav = document.querySelector('nav');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > lastScroll && currentScroll > 100) {
            // Scrolling down & past the header
            nav.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            nav.style.transform = 'translateY(0)';
        }

        lastScroll = currentScroll;
    });
});

// Add dynamic theme switching based on time of day
const updateTheme = () => {
    const hour = new Date().getHours();
    const root = document.documentElement;
    
    if (hour >= 18 || hour < 6) {
        // Night theme
        root.style.setProperty('--primary-color', '#1a2634');
        root.style.setProperty('--text-color', '#ffffff');
        root.style.setProperty('--light-bg', '#2c3e50');
        document.body.style.background = 'linear-gradient(135deg, #1a2634 0%, #2c3e50 100%)';
    } else {
        // Day theme
        root.style.setProperty('--primary-color', '#2c3e50');
        root.style.setProperty('--text-color', '#34495e');
        root.style.setProperty('--light-bg', '#ecf0f1');
        document.body.style.background = 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)';
    }
};

// Update theme immediately and every hour
updateTheme();
setInterval(updateTheme, 3600000); // Check every hour