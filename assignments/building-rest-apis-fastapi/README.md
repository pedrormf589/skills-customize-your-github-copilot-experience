# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and practice creating endpoints, request/response models, and basic CRUD operations. By the end, you will structure a small backend service that validates data and returns consistent JSON responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Descrição
Create the FastAPI app entry point and define a simple health-check endpoint.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app instance in `starter-code.py`
- Expose a `GET /health` endpoint returning `{ "status": "ok" }`
- Run locally with Uvicorn and respond successfully in the browser or API docs

### 🛠️ Create Item Models and In-Memory Storage

#### Descrição
Define data models using Pydantic and store items in memory for API operations.

#### Requisitos
O programa concluído deve:

- Define an `ItemCreate` model with fields `name` and `price`
- Define an `Item` model with fields `id`, `name`, and `price`
- Use a Python list (or dictionary) as in-memory storage
- Ensure invalid payloads are rejected by FastAPI validation

### 🛠️ Implement CRUD Endpoints

#### Descrição
Implement REST endpoints to create, list, update, and delete items.

#### Requisitos
O programa concluído deve:

- Implement `POST /items` to create a new item with auto-generated `id`
- Implement `GET /items` to list all items
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item
- Return `404` when trying to update or delete a non-existent item

### 🛠️ Add Query Filtering

#### Descrição
Enhance the listing endpoint to support basic filtering through query parameters.

#### Requisitos
O programa concluído deve:

- Add an optional query parameter `min_price` to `GET /items`
- Return only items with `price >= min_price` when the parameter is provided
- Keep default behavior returning all items when no filter is passed
