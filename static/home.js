document.addEventListener("DOMContentLoaded", function () {
      // Simulate fetching user data
      const userData = {
        username: "Astroboy",
        profilePicture: "profile.jpg", // Replace with actual user profile picture URL
        status: "Active",
        details: [
          { id: 1, name: "John Doe", status: "Active" },
          { id: 2, name: "Jane Smith", status: "Inactive" }
        ]
      };

      // Update profile details
      document.getElementById("username").textContent = userData.username;
      document.getElementById("username-card").textContent = userData.username;
      document.getElementById("profile-picture").src = userData.profilePicture;
      document.getElementById("user-status").textContent = userData.status;

      // Populate user details table
      const detailsTable = document.getElementById("user-details");
      userData.details.forEach(detail => {
        const row = `
          <tr>
            <td>${detail.id}</td>
            <td>${detail.name}</td>
            <td>${detail.status}</td>
          </tr>
        `;
        detailsTable.insertAdjacentHTML("beforeend", row);
      });
    });
