function checkPassword() {
    const passwordInput = document.getElementById("password");
    const resultDiv = document.getElementById("result");

    if (passwordInput.value.length == 0) {
        Swal.fire({
            icon: 'error',
            title: 'No Input...',
            text: 'Kindly enter the Password !',
          })
          
        return 
    }
    const password = passwordInput.value;
    

    // Define password policies (equivalent to the Python code)
    const min_length = 8;
    const min_uppercase = 1;
    const min_lowercase = 1;
    const min_digits = 1;
    const min_special_chars = 1;
    const common_passwords = ['password', '123456', 'qwerty', 'abc123'];

    if (common_passwords.includes(password)){
        Swal.fire(
            `Common Password`,
            "<h3>Your password is too common    </h3>",
            'error'
          )
        return
    }

    // Initialize a score for the password
    let score = 0;

    // Check minimum length
    if (password.length >= min_length) {
        score += 1;
    }

    // Check for uppercase letters
    if (password.match(/[A-Z]/g) && password.match(/[A-Z]/g).length >= min_uppercase) {
        score += 1;
    }

    // Check for lowercase letters
    if (password.match(/[a-z]/g) && password.match(/[a-z]/g).length >= min_lowercase) {
        score += 1;
    }

    // Check for digits
    if (password.match(/[0-9]/g) && password.match(/[0-9]/g).length >= min_digits) {
        score += 1;
    }

    // Check for special characters (you can define your own set)
    if (password.match(/[!@#$%^&*()]/g) && password.match(/[!@#$%^&*()]/g).length >= min_special_chars) {
        score += 1;
    }

    // Check if the password is not a common one
    if (!common_passwords.includes(password)) {
        score += 1;
    }

    // Calculate entropy (equivalent to the Python code)
    const entropy = calculateEntropy(password);

    // Check if the password has high entropy (adjust this threshold as needed)
    if (entropy >= 3.0) {
        score += 1;
    }

    // Display the result
    if (score >= 6) {
        resultDiv.innerText = "Password is strong!";
        resultDiv.style.color = "green";
        Swal.fire(
            `Entropy: ${entropy.toFixed(2)}`,
            "<h3>Your password is Strong</h3>",
            'success'
          )
    } else {
        resultDiv.innerText = "Password is weak.";
        resultDiv.style.color = "red";
        Swal.fire(
            `Entropy: ${entropy.toFixed(2)}`,
            "<h3>Your password is weak</h3>",
            'warning'
          )
    }

    resultDiv.innerHTML += `<br>Entropy: ${entropy.toFixed(2)}`;
}

function calculateEntropy(password) {
    // Calculate the entropy of the password (equivalent to the Python code)
    const charSetSize = [...new Set(password)].length;
    let entropy = 0.0;

    if (charSetSize > 0) {
        entropy = Math.log2(Math.pow(charSetSize, password.length));
    }

    return entropy;
}

function clearBox() {
    let passwordInput = document.getElementById("password");
    let resultDiv = document.getElementById("result");
    passwordInput.value = ''
    resultDiv.innerText = ''
  }
