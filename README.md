# book-store

book-store designed for the devOps capstone assignment

# Features

- Crud API for book
- PostgreSQL database backend
- Containerized with Docker and Docker Compose
- CI/CD pipeline with GitHub Actions and semantic-release
- Helm Chart for Kubernetes deployment
- Managed with Argo CD

# Steps to use the project

1. Clone the repository:

```bash 
$ git clone https://github.com/nayaradima/book-store.git
$ cd book-store
```
2. Build and run with docker compose:

```bash
$ docker-compose up --build
```
3. Testing:

```bash
$ python manage.py pytest
```

4. Open the browser and access the API at http://localhost:8000/api/books/

5. Deployment:

- Deployed with Helm Chart
- Managed via Argo CD for syncing with Kubernetes


