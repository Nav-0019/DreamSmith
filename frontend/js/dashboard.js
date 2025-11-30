/**
 * Dashboard JavaScript
 * Handles user data fetching, display, and logout functionality
 */

/**
 * Fetch and display current user data
 */
async function loadUserData() {
    const token = localStorage.getItem(STORAGE_KEYS.accessToken);

    // If no token, redirect to login
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    try {
        const response = await fetch(API_ENDPOINTS.me, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const userData = await response.json();

            // Display user data
            document.getElementById('userGreeting').textContent = `Hello, ${userData.username}!`;
            document.getElementById('userUsername').textContent = userData.username;
            document.getElementById('userEmail').textContent = userData.email;
            document.getElementById('userId').textContent = `#${userData.id}`;

            // Format created_at date
            const createdDate = new Date(userData.created_at);
            document.getElementById('userCreatedAt').textContent = createdDate.toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });

        } else {
            // Token is invalid or expired
            console.error('Failed to fetch user data');
            logout();
        }

    } catch (error) {
        console.error('Error loading user data:', error);
        // Show error but don't logout - might be network issue
        document.getElementById('userGreeting').textContent = 'Error loading data';
    }
}

/**
 * Handle Logout
 */
function logout() {
    // Clear localStorage
    localStorage.removeItem(STORAGE_KEYS.accessToken);
    localStorage.removeItem(STORAGE_KEYS.tokenType);

    // Redirect to login page
    window.location.href = 'login.html';
}

/**
 * Initialize Dashboard
 */
function initDashboard() {
    // Load user data
    loadUserData();

    // Setup logout button
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', logout);
    }
}

// Initialize on page load
if (typeof window !== 'undefined') {
    window.addEventListener('load', initDashboard);
}
