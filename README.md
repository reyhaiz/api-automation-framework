# 🧪 API Automation Framework

A Python-based API test automation framework built with **pytest**, designed to validate REST API endpoints with comprehensive coverage including positive, negative, and boundary test cases.

---

## 📋 Overview

This framework automates testing of RESTful APIs and validates response status codes, schemas, payloads, response times, and content types. It is structured around resource-based test modules and generates rich HTML reports using `pytest-html`.

**Current test target:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free fake REST API used for testing and prototyping.

---

## ✅ Test Results

| Metric | Value |
|---|---|
| Total Tests | 30 |
| Passed | ✅ 30 |
| Failed | ❌ 0 |
| Skipped | ⏭️ 0 |
| Total Duration | ~7 seconds |

---

## 📁 Project Structure

```
api-automation-framework/
├── tests/
│   ├── test_posts.py       # Tests for /posts endpoint
│   └── test_users.py       # Tests for /users endpoint
├── reports/
│   └── report_all.html     # Generated HTML test report
├── conftest.py             # Shared fixtures and configuration
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🧪 Test Coverage

### `test_posts.py` — `/posts` Endpoint

| Class | Test | Description |
|---|---|---|
| `TestGetPosts` | `test_get_all_posts_status_200` | GET all posts returns 200 |
| `TestGetPosts` | `test_get_all_posts_returns_100_items` | Response contains 100 items |
| `TestGetPosts` | `test_get_all_posts_response_time` | Response time is within threshold |
| `TestGetPosts` | `test_get_all_posts_content_type_json` | Content-Type is `application/json` |
| `TestGetPosts` | `test_get_post_by_id_status_200` | GET single post by ID returns 200 |
| `TestGetPosts` | `test_get_post_by_id_correct_schema` | Response schema is valid |
| `TestGetPosts` | `test_get_post_by_id_correct_value` | Response payload values are correct |
| `TestGetPosts` | `test_filter_posts_by_userid` | Filter posts by `userId` query param |
| `TestCreatePost` | `test_create_post_status_201` | POST new post returns 201 |
| `TestCreatePost` | `test_create_post_returns_id` | New post response includes an `id` |
| `TestCreatePost` | `test_create_post_title_matches` | Response title matches request body |
| `TestUpdatePost` | `test_put_post_status_200` | PUT full update returns 200 |
| `TestUpdatePost` | `test_patch_post_title_updated` | PATCH partial update reflects new title |
| `TestDeletePost` | `test_delete_post_status_200` | DELETE returns 200 |
| `TestDeletePost` | `test_delete_post_empty_response` | DELETE response body is empty |
| `TestNegativePosts` | `test_get_nonexistent_post_404` | Non-existent post ID returns 404 |
| `TestNegativePosts` | `test_get_post_string_id_404` | String ID returns 404 |
| `TestNegativePosts` | `test_get_post_negative_id_404` | Negative ID returns 404 |
| `TestBoundaryPosts` | `test_get_first_post_id_1` | First valid post (ID=1) is accessible |
| `TestBoundaryPosts` | `test_get_last_post_id_100` | Last valid post (ID=100) is accessible |
| `TestBoundaryPosts` | `test_get_post_id_101_not_found` | Out-of-range ID (101) returns 404 |
| `TestBoundaryPosts` | `test_create_post_empty_title` | Create post with empty title |
| `TestBoundaryPosts` | `test_create_post_very_long_title` | Create post with very long title |

### `test_users.py` — `/users` Endpoint

| Class | Test | Description |
|---|---|---|
| `TestGetUsers` | `test_get_all_users_status_200` | GET all users returns 200 |
| `TestGetUsers` | `test_get_all_users_returns_10` | Response contains 10 users |
| `TestGetUsers` | `test_get_user_by_id_valid_schema` | User response matches expected schema |
| `TestGetUsers` | `test_get_user_posts_not_empty` | User has at least one associated post |
| `TestGetUsers` | `test_get_nonexistent_user_404` | Non-existent user returns 404 |
| `TestGetUsers` | `test_get_first_user_id_1` | First user (ID=1) is accessible |
| `TestGetUsers` | `test_get_last_user_id_10` | Last user (ID=10) is accessible |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.13 | Language |
| pytest | 8.3.5 | Test runner |
| pytest-html | 4.2.0 | HTML report generation |
| pytest-base-url | 2.1.0 | Base URL configuration |
| pytest-metadata | 3.1.1 | Report metadata |
| Faker | 40.8.0 | Test data generation |
| pytest-playwright | 0.5.1 | Browser automation (optional) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/reyhaiz/api-automation-framework.git
cd api-automation-framework

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report_all.html --self-contained-html

# Run a specific test file
pytest tests/test_posts.py

# Run a specific test class
pytest tests/test_posts.py::TestGetPosts

# Run with verbose output
pytest -v

# Run with base URL override
pytest --base-url=https://jsonplaceholder.typicode.com
```

---

## 📊 HTML Report

After running the tests, open the generated report:

```bash
open reports/report_all.html
# or on Windows:
start reports/report_all.html
```

The report includes sortable/filterable results, test durations, logs, and environment metadata.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/add-comments-tests`)
3. Commit your changes (`git commit -m 'Add tests for /comments endpoint'`)
4. Push to the branch (`git push origin feature/add-comments-tests`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
