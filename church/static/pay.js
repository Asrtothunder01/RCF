// Wait until DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".payment-local");
  const bankNameInput = document.getElementById("bank-used");
  const accountNumberInput = document.getElementById("bank-account-number");
  const submitButton = document.getElementById("submit");

  // Validate bank name (no numbers, special characters)
  const validateBankName = (name) => /^[a-zA-Z\s]+$/.test(name);

  // Validate account number (digits only, length between 10-15)
  const validateAccountNumber = (number) => /^\d{10,15}$/.test(number);

  // Show error message
  const showError = (input, message) => {
    let error = input.nextElementSibling;
    if (!error || error.className !== "error-message") {
      error = document.createElement("p");
      error.className = "error-message";
      input.parentElement.appendChild(error);
    }
    error.textContent = message;
    error.style.color = "red";
    input.style.borderColor = "red";
  };

  // Clear error message
  const clearError = (input) => {
    const error = input.nextElementSibling;
    if (error && error.className === "error-message") {
      error.remove();
    }
    input.style.borderColor = "";
  };

  // Add event listeners to inputs for validation
  bankNameInput.addEventListener("input", () => {
    if (!validateBankName(bankNameInput.value.trim())) {
      showError(bankNameInput, "Bank name should only contain letters.");
    } else {
      clearError(bankNameInput);
    }
  });

  accountNumberInput.addEventListener("input", () => {
    if (!validateAccountNumber(accountNumberInput.value.trim())) {
      showError(accountNumberInput, "Account number must be 10-15 digits.");
    } else {
      clearError(accountNumberInput);
    }
  });

  // Handle form submission
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const bankName = bankNameInput.value.trim();
    const accountNumber = accountNumberInput.value.trim();

    // Validate fields before submission
    if (!validateBankName(bankName)) {
      showError(bankNameInput, "Bank name is invalid.");
      return;
    }

    if (!validateAccountNumber(accountNumber)) {
      showError(accountNumberInput, "Account number is invalid.");
      return;
    }

    // Show confirmation dialog
    const confirmPayment = confirm(
      `Confirm payment details:\nBank: ${bankName}\nAccount Number: ${accountNumber}`
    );

    if (confirmPayment) {
      alert("Payment details submitted successfully!");
      form.reset(); // Clear form after submission
    }
  });

  // Add mobile responsiveness for the toolbar (optional)
  const toolbar = document.querySelector(".toolbar");
  window.addEventListener("resize", () => {
    if (window.innerWidth < 768) {
      toolbar.style.padding = "10px";
    } else {
      toolbar.style.padding = "20px";
    }
  });
});
