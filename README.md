## Installation
- Copy the repository
- Create .env file with following variables:
    - FLASK_DEBUG=1
    - SQLALCHEMY_DATABASE_URI="postgresql://......"

- Run the following commands:
    - `pipenv install`
    - `pipenv shell`
    - `python seed.py`

## Running
- Run the following command:
- `python app.py`
- The system should run on http://localhost:4000/

## Testing
- Run the following commands:
    - `pipenv run test`
    - `pipenv run coverage`

## Available endpoints
- "GET /",
- "GET /authors",
- "GET /authors/<int:id>",
- "POST /authors",
- "PATCH /authors/<int:id>",
- "DELETE /authors/<int:id>",
- "GET /books",
- "GET /books/<int:id>",
- "POST /books",
- "PATCH /books/<int:id>",
- "DELETE /books/<int:id>"
