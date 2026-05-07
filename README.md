## fastapi-crud-api

REST API built with FastAPI in Python that implements a full CRUD over a list of items.

Personal project built to learn and practice REST API development with FastAPI.

---

## Technologies

- Python 3.10
- FastAPI
- Uvicorn
- Pydantic

---

## How to install and run

```bash
# Clone the repository
git clone https://github.com/FMancaDev/FastAPI_Crud_API.git
cd FastAPI_Crud_API

# Run the installer
make install

# Start the server
make run
```

The API will be available at `http://localhost:8000`

The interactive documentation (Swagger UI) will be available at `http://localhost:8000/docs`

### Other commands

| Command | Description |
|---------|-------------|
| `make install` | Creates the virtual environment and installs dependencies |
| `make run` | Starts the server |
| `make freeze` | Updates requirements.txt with current dependencies |
| `make clean` | Removes the virtual environment |

---

## What is an endpoint?

An endpoint is an access point of the API — it is a path (URL) that the server exposes to receive requests. Each endpoint has an associated HTTP method that defines the type of operation:

- **GET** — fetch/read data
- **POST** — create something new
- **PUT** — update something existing
- **DELETE** — delete something

---

## Available endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Confirms the API is online |
| GET | `/items` | Returns the full list of items |
| GET | `/items/{item_id}` | Returns a specific item by its id. Returns 404 if not found |
| POST | `/items` | Creates a new item. The `name` field is required (between 2 and 17 characters) |
| PUT | `/items/{item_id}` | Updates the name of an existing item by its id. Returns 404 if not found |
| DELETE | `/items/{item_id}` | Removes an item by its id. Returns 404 if not found |

---

## Project structure

```
fastapi-crud-api/
├── minha_api/
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── Makefile
├── README.md
└── .gitignore
```
