/**
 * Authentication JavaScript for Login and Signup
 * Handles form submissions, API calls, and token management
 */

/**
 * Handle Login Form Submission
 */
async function handleLogin(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const loginButton = document.getElementById('loginButton');
    const errorMessage = document.getElementById('errorMessage');
    const successMessage = document.getElementById('successMessage');

    // Hide previous messages
    errorMessage.classList.add('hidden');
    successMessage.classList.add('hidden');

    // Disable button and show loading
    loginButton.disabled = true;
    loginButton.textContent = 'Logging in...';

    try {
        const response = await fetch(API_ENDPOINTS.login, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            // Store token in localStorage
            localStorage.setItem(STORAGE_KEYS.accessToken, data.access_token);
            localStorage.setItem(STORAGE_KEYS.tokenType, data.token_type);

            // Show success message
            successMessage.classList.remove('hidden');
            document.getElementById('successText').textContent = 'Login successful! Redirecting...';

            // Redirect to dashboard after 1 second
            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 1000);

        } else {
            // Show error message
            errorMessage.classList.remove('hidden');
            document.getElementById('errorText').textContent = data.detail || 'Login failed. Please check your credentials.';

            // Re-enable button
            loginButton.disabled = false;
            loginButton.textContent = 'Login';
        }

    } catch (error) {
        console.error('Login error:', error);
        errorMessage.classList.remove('hidden');
        document.getElementById('errorText').textContent = 'Network error. Please check if the backend server is running.';

        // Re-enable button
        loginButton.disabled = false;
        loginButton.textContent = 'Login';
    }
}

/**
 * Handle Signup Form Submission
 */
async function handleSignup(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const signupButton = document.getElementById('signupButton');
    const errorMessage = document.getElementById('errorMessage');
    const successMessage = document.getElementById('successMessage');

    // Hide previous messages
    errorMessage.classList.add('hidden');
    successMessage.classList.add('hidden');

    // Disable button and show loading
    signupButton.disabled = true;
    signupButton.textContent = 'Creating Account...';

    try {
        const response = await fetch(API_ENDPOINTS.register, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        const data = await response.json();

        if (response.ok) {
            // Show success message
            successMessage.classList.remove('hidden');
            document.getElementById('successText').textContent = 'Account created successfully! Redirecting to login...';

            // Redirect to login after 2 seconds
            setTimeout(() => {
                window.location.href = 'login.html';
            }, 2000);

        } else {
            // Show error message
            errorMessage.classList.remove('hidden');
            document.getElementById('errorText').textContent = data.detail || 'Signup failed. Please try again.';

            // Re-enable button
            signupButton.disabled = false;
            signupButton.textContent = 'Create Account';
        }

    } catch (error) {
        console.error('Signup error:', error);
        errorMessage.classList.remove('hidden');
        document.getElementById('errorText').textContent = 'Network error. Please check if the backend server is running.';

        // Re-enable button
        signupButton.disabled = false;
        signupButton.textContent = 'Create Account';
    }
}

/**
 * Check if user is already logged in
 * Redirect to dashboard if token exists
 */
function checkIfLoggedIn() {
    const token = localStorage.getItem(STORAGE_KEYS.accessToken);

    // If on login/signup page and already logged in, redirect to dashboard
    if (token && (window.location.pathname.includes('login.html') || window.location.pathname.includes('signup.html'))) {
        window.location.href = 'dashboard.html';
    }
}

// Check login status on page load
if (typeof window !== 'undefined') {
    window.addEventListener('load', checkIfLoggedIn);
}
