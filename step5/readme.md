1. Added additional models to model/book.py
2. Added controller/book.py, this is pretty much a copy of controller/author.py
3. Connected BookController to route handler in main.py

### litestar --app step4.main:app run ###

### OpenAPI site can be accessed via: ###
   - http://localhost:8000/docs
   - http://localhost:8000/docs/swagger
   - http://localhost:8000/docs/elements
   - http://localhost:8000/docs/redoc
   - http://localhost:8000/docs/rapidoc