// JavaScript for Products - Church Store
document.addEventListener("DOMContentLoaded", () => {
    // Sample products
    const products = [
        { name: "Bible", description: "Holy Bible for daily use.", price: 15.99, img: "https://via.placeholder.com/150" },
        { name: "Hymn Book", description: "Collection of church hymns.", price: 9.99, img: "https://via.placeholder.com/150" },
        { name: "Event Ticket", description: "Ticket for church events.", price: 20.00, img: "https://via.placeholder.com/150" },
        { name: "Devotional Book", description: "Daily devotional for Christians.", price: 12.50, img: "https://via.placeholder.com/150" },
        { name: "T-Shirt", description: "Customized church T-shirt.", price: 18.00, img: "https://via.placeholder.com/150" },
        { name: "Worship CD", description: "Collection of worship songs.", price: 10.00, img: "https://via.placeholder.com/150" }
    ];

    const productContainer = document.querySelector(".row");

    // Dynamically generate product cards
    products.forEach(product => {
        const productCard = `
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <img src="${product.img}" class="card-img-top" alt="${product.name}">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">${product.description}</p>
                        <p class="text-muted">Price: $${product.price.toFixed(2)}</p>
                        <a href="pay.html" class="btn btn-primary">Buy Now</a>
                    </div>
                </div>
            </div>
        `;
        productContainer.innerHTML += productCard;
    });

    // Search functionality
    const header = document.querySelector("header");
    const searchContainer = document.createElement("div");
    searchContainer.innerHTML = `
        <input type="text" id="searchInput" class="form-control mt-4" placeholder="Search for products..." />
    `;
    header.appendChild(searchContainer);

    const searchInput = document.getElementById("searchInput");
    searchInput.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase();
        const filteredProducts = products.filter(product =>
            product.name.toLowerCase().includes(query) || product.description.toLowerCase().includes(query)
        );

        productContainer.innerHTML = ""; // Clear current products
        filteredProducts.forEach(product => {
            const productCard = `
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <img src="${product.img}" class="card-img-top" alt="${product.name}">
                        <div class="card-body">
                            <h5 class="card-title">${product.name}</h5>
                            <p class="card-text">${product.description}</p>
                            <p class="text-muted">Price: $${product.price.toFixed(2)}</p>
                            <a href="pay.html" class="btn btn-primary">Buy Now</a>
                        </div>
                    </div>
                </div>
            `;
            productContainer.innerHTML += productCard;
        });
    });

    // Mobile navigation toggle enhancement
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarNav = document.querySelector("#navbarNav");
    navbarToggler.addEventListener("click", () => {
        navbarNav.classList.toggle("show");
    });

    console.log("JavaScript is locked and loaded 🚀");
});￼Enter
