// --- Early Theme Initializer ---
(function() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
    }
})();

function toggleTheme() {
    const body = document.body;
    const btn = document.getElementById('theme-toggle-btn');
    if (body.classList.contains('light-theme')) {
        body.classList.remove('light-theme');
        localStorage.setItem('theme', 'dark');
        if (btn) btn.textContent = '☀️';
    } else {
        body.classList.add('light-theme');
        localStorage.setItem('theme', 'light');
        if (btn) btn.textContent = '🌙';
    }
}

const API_BASE = 'http://127.0.0.1:8000';

// --- Session & Auth Helpers ---
function getSessionUser() {
    const userStr = localStorage.getItem('taxi_user');
    return userStr ? JSON.parse(userStr) : null;
}

function setSessionUser(user) {
    localStorage.setItem('taxi_user', JSON.stringify(user));
}

function clearSession() {
    localStorage.removeItem('taxi_user');
    window.location.href = 'login.html';
}

// --- Notification Toast ---
function showNotification(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) {
        const div = document.createElement('div');
        div.id = 'toast-container';
        div.className = 'toast-container';
        document.body.appendChild(div);
    }
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span>${message}</span>
        <button class="modal-close" style="font-size: 1.1rem; margin-left: 1rem;" onclick="this.parentElement.remove()">&times;</button>
    `;
    
    document.getElementById('toast-container').appendChild(toast);
    
    // Auto-remove after 4 seconds
    setTimeout(() => {
        toast.remove();
    }, 4000);
}

// --- API Fetch Wrapper ---
async function fetchAPI(endpoint, method = 'GET', body = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    if (body) {
        options.body = JSON.stringify(body);
    }
    
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || `HTTP error! Status: ${response.status}`);
        }
        return data;
    } catch (error) {
        console.error(`API Error on ${endpoint}:`, error);
        showNotification(error.message, 'error');
        throw error;
    }
}

// --- Navbar Initializer ---
function initNavbar() {
    const navLinks = document.getElementById('nav-links');
    if (!navLinks) return;
    
    const user = getSessionUser();
    
    let html = `<li><a href="index.html">Home</a></li>`;
    
    if (user) {
        if (user.role === 'customer') {
            html += `
                <li><a href="booking.html">Book Ride</a></li>
                <li><a href="ride_history.html">Ride History</a></li>
                <li><a href="customer_dashboard.html">Dashboard</a></li>
            `;
        } else if (user.role === 'driver') {
            html += `
                <li><a href="drivers.html">My Trips</a></li>
                <li><a href="driver_dashboard.html">Dashboard</a></li>
            `;
        } else if (user.role === 'admin') {
            html += `
                <li><a href="admin_dashboard.html">Admin Console</a></li>
            `;
        }
        
        html += `
            <li style="margin-left: 1.5rem; color: var(--accent); font-weight: 600;">
                Hello, ${user.name} (${user.role})
            </li>
            <li><a href="#" onclick="clearSession()" class="nav-btn-secondary" style="margin-left: 0.5rem;">Logout</a></li>
        `;
    } else {
        html += `
            <li><a href="login.html" class="nav-btn-secondary">Login</a></li>
            <li><a href="register.html" class="nav-btn">Register</a></li>
        `;
    }

    // Append Theme Switcher
    const currentTheme = localStorage.getItem('theme') || 'dark';
    const themeIcon = currentTheme === 'light' ? '🌙' : '☀️';
    html += `
        <li style="margin-left: 1rem;">
            <button onclick="toggleTheme()" id="theme-toggle-btn" class="nav-btn-secondary" style="padding: 0.4rem 0.8rem; border-radius: 12px; font-size: 1rem; cursor: pointer; display: flex; align-items: center; justify-content: center;">
                ${themeIcon}
            </button>
        </li>
    `;
    
    navLinks.innerHTML = html;
    
    // Highlight active link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const links = navLinks.querySelectorAll('a');
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.add('active');
        }
    });
}

// Ensure navbar is loaded
document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
});
