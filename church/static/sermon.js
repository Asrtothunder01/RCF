// sermon.js

document.addEventListener("DOMContentLoaded", () => {
    // 1. Voice Search for Sermons
    const voiceSearchBtn = document.createElement("button");
    voiceSearchBtn.className = "btn btn-outline-secondary my-3";
    voiceSearchBtn.innerText = "Search Sermons by Voice";
    voiceSearchBtn.style.display = "block";
    voiceSearchBtn.style.margin = "0 auto";
    document.querySelector(".container").prepend(voiceSearchBtn);

    voiceSearchBtn.addEventListener("click", () => {
        if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.lang = "en-US";
            recognition.start();

            recognition.onresult = (event) => {
                const query = event.results[0][0].transcript.toLowerCase();
                searchSermons(query);
            };

            recognition.onerror = () => {
                alert("Voice recognition failed. Please try again.");
            };
        } else {
            alert("Voice search is not supported in your browser.");
        }
    });

    // 2. Live Sermon Notifications
    const sermons = [
        { title: "Faith and Perseverance", date: "2024-12-24", preacher: "John Doe", theme: "Faith" },
        { title: "Hope in Hard Times", date: "2025-01-10", preacher: "Jane Smith", theme: "Hope" },
        { title: "The Power of Forgiveness", date: "2025-02-15", preacher: "Paul Johnson", theme: "Forgiveness" }
    ];

    const upcomingSermons = sermons.filter(sermon => new Date(sermon.date) > new Date());

    if ("Notification" in window && Notification.permission === "default") {
        Notification.requestPermission();
    }

    if ("Notification" in window && Notification.permission === "granted") {
        upcomingSermons.forEach(sermon => {
            const sermonDate = new Date(sermon.date);
            const now = new Date();

            if ((sermonDate - now) < 24 * 60 * 60 * 1000) { // Within 24 hours
                new Notification("Upcoming Sermon!", {
                    body: `${sermon.title} by ${sermon.preacher} on ${sermon.date}`,
                    icon: "https://cdn-icons-png.flaticon.com/512/2598/2598801.png"
                });
            }
        });
    }

    // 3. Search Functionality
    function searchSermons(query) {
        const cards = document.querySelectorAll(".card");
        cards.forEach(card => {
            const title = card.querySelector(".card-title").innerText.toLowerCase();
            const theme = card.querySelector(".card-text:nth-child(4)").innerText.toLowerCase();
            if (title.includes(query) || theme.includes(query)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    }

    // 4. Bookmark Sermons
    document.querySelectorAll(".card .btn-secondary").forEach((button, index) => {
        button.addEventListener("click", () => {
            const sermonTitle = sermons[index]?.title || "Sermon Title";
            const bookmarks = JSON.parse(localStorage.getItem("bookmarkedSermons") || "[]");
            if (!bookmarks.includes(sermonTitle)) {
                bookmarks.push(sermonTitle);
                localStorage.setItem("bookmarkedSermons", JSON.stringify(bookmarks));
                alert(`"${sermonTitle}" has been bookmarked!`);
            } else {
                alert(`"${sermonTitle}" is already bookmarked.`);
            }
        });
    });

    // 5. Display Bookmarked Sermons
    const bookmarksBtn = document.createElement("button");
    bookmarksBtn.className = "btn btn-outline-info my-3";
    bookmarksBtn.innerText = "View Bookmarked Sermons";
    bookmarksBtn.style.display = "block";
    bookmarksBtn.style.margin = "0 auto";
    document.querySelector(".container").appendChild(bookmarksBtn);

    bookmarksBtn.addEventListener("click", () => {
        const bookmarks = JSON.parse(localStorage.getItem("bookmarkedSermons") || "[]");
        if (bookmarks.length > 0) {
            alert("Bookmarked Sermons:\n" + bookmarks.join("\n"));
        } else {
            alert("No sermons bookmarked yet.");
        }
    });
})
