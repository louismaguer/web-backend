# 🔐 web authentication

a summary of various common web authentication techniques

## Session-based Authentication

- User submits login credentials
- Server creates a session and stores it in memory or DB
- Server sends a session ID as a cookie

Example:

```http
POST /login
→ Set-Cookie: session_id=abc123
```

Subsequent requests include the session ID:

```http
GET /profile
Cookie: session_id=abc123
```

---

## API Key Authentication

- Simple string used to authenticate requests
- Often used for server-to-server communication
- You typically get the API key when you register with the service
  - e.g. google maps, assemblyAI, scaleway, etc..

Example:

```http
GET /data
x-api-key: abc123xyz456
```

---

## Token-based Authentication (JWT)

- User logs in, receives a signed JWT
- Client stores token (e.g., in localStorage)
- Token sent in headers with each request
- Token is parsable and self-contained

Example:

```http
 GET /profile
Authorization: Bearer eyJhbGciOi...
```

---

## 🔗 OAuth 2.0

OAuth is about Delegated Access:

- Used for "Login with Google" / "Login with GitHub"
- User authorizes third-party app via identity provider

Basic flow:

1. App redirects to provider’s auth page
2. User logs in and consents
3. Provider redirects back with a `code`
4. App exchanges code for access token

Example exchange:

```http
POST /oauth/token
→ { "access_token": "abc123" }
```

---

## 🔒 Multi-Factor Authentication (MFA)

- Adds extra layer beyond just passwords
- Combines two or more of:
  - Something you know (password)
  - Something you have (phone, token)
  - Something you are (biometrics)

Examples:
- SMS or app-based 6-digit codes
- U2F hardware keys (e.g. YubiKey)

    > Enter 6-digit code: 493021

Greatly reduces the risk of compromised accounts
