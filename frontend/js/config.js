/**
 * Configuration file for MoneySeed application
 * Contains API endpoints and shared constants
 */

// API Base URL - Empty string for relative paths (same origin)
const API_BASE_URL = '';

// API Endpoints
const API_ENDPOINTS = {
    register: `${API_BASE_URL}/auth/register`,
    login: `${API_BASE_URL}/auth/login`,
    me: `${API_BASE_URL}/auth/me`,
    root: `${API_BASE_URL}/`
};

// Local Storage Keys
const STORAGE_KEYS = {
    accessToken: 'access_token',
    tokenType: 'token_type'
};
