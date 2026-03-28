# Items API Documentation

## Introduction

This API is a simple RESTful service that demonstrates core API concepts, including routing, pagination, CORS configuration, and error handling. It exposes a single resource—`items`—and allows clients to retrieve a paginated list of items using standard HTTP requests. The API is designed for educational purposes and does not require authentication.

---

## Getting Started

### Base URL

When running locally, the API is available at:

```
http://127.0.0.1:5000
```

All endpoints described below are relative to this base URL.

### API Keys / Authentication

This API does **not** require authentication. All endpoints are publicly accessible.

---

## Errors

The API returns JSON-formatted error responses with appropriate HTTP status codes.

### Response Codes

| Status Code | Meaning |
|------------|--------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

### Messages

Error responses follow a consistent structure:

```json
{
  "error": "Error type",
  "message": "Human-readable explanation"
}
```

### Error Types

| Error | Description |
|------|------------|
| Invalid pagination parameters | `page` or `per_page` is less than 1 |
| Not Found | The requested endpoint does not exist |
| Internal Server Error | An unexpected server-side error |

---

## Resource Endpoint Library

### Resource: Items

The `items` resource represents a collection of item names stored on the server.

---

### GET `/items`

Retrieve a paginated list of items.

#### Sample Request

```
GET /items?page=2&per_page=3
```

#### Arguments

| Name | Location | Type | Required | Default | Description |
|-----|----------|------|----------|---------|-------------|
| `page` | Query | Integer | No | 1 | Page number to retrieve |
| `per_page` | Query | Integer | No | 3 | Number of items per page |

---

#### Successful Response

**Status Code:** `200 OK`

```json
{
  "page": 2,
  "per_page": 3,
  "total_items": 10,
  "items": ["donut", "egg", "fig"]
}
```

#### Response Object

| Field | Type | Description |
|------|------|-------------|
| `page` | Integer | Current page number |
| `per_page` | Integer | Number of items per page |
| `total_items` | Integer | Total number of available items |
| `items` | Array of Strings | Items for the requested page |

---

#### Error Responses

**Invalid pagination parameters**

**Status Code:** `400 Bad Request`

```json
{
  "error": "Invalid pagination parameters",
  "message": "page and per_page must be positive integers"
}
```

---

## Global Errors

### 404 – Not Found

Returned when a non-existent endpoint is requested.

```json
{
  "error": "Not Found",
  "message": "The requested resource does not exist"
}
```

### 500 – Internal Server Error

Returns when an unexpected server error occurs.

```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```

---

## Notes on CORS

This API enables Cross-Origin Resource Sharing (CORS), allowing access from web applications running on different domains. Common HTTP methods and headers are explicitly allowed to support browser-based clients and preflight (`OPTIONS`) requests.

---

## Summary

This API demonstrates a minimal but complete REST interface, including pagination, structured error handling, and CORS support. It serves as a foundation for building more complex APIs with authentication, additional resources, and persistent data storage.
