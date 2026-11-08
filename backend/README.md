# Optional FastAPI starter

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API docs: http://127.0.0.1:8000/docs

This is a shared starter API scaffold. It returns sample data and a placeholder support draft. It does not persist records or connect to an AI provider. Add a database, authentication, validation, tests and provider integration before production.
