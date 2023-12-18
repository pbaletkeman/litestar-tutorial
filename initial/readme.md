Taken directly from https://docs.litestar.dev/latest/tutorials/repository-tutorial/03-repository-controller.html

1. setup Python Poetry
2. add the following lines under '[tool.poetry.dependencies]' in pyproject.py
   - pydantic = {extras = ["email"], version = "^2.5.2"}
   - litestar = {extras = ["sqlalchemy", "standard"], version = "^2.4.4"}
   - aiosqlite = "^0.19.0"
   - sqlalchemy = "^2.0.23"
3. activate poetry environment
4. command line execute `litestar --app inital.app:app run`
5. OpenAPI site can be accessed via:
   - http://localhost:8000/schema
   - http://localhost:8000/schema/swagger
   - http://localhost:8000/schema/elements
   - http://localhost:8000/schema/redoc
   - http://localhost:8000/schema/rapidoc
   