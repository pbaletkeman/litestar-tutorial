***Table Of Contents***
1. ### rename app.py to main.py ####
2. ### refactor to extract controller related parts into a controller file ####
3. ### refactor to extract the model related parts into model files ####
4. ### refactor to extract common/shared elements into their own file ####

## rename app.py to main.py ###
   - to reduce the number of 'app's in the command
   - run command becomes `litestar --app step1.main:app run`
     - `--app` used to specify the litestar application
     - `step1.main` is the full package path to the litestar application
     - `app` is the name of your litestar application module
     - `run` is the command to execute
## refactor to extract controller related parts into a controller file ###
1. created Python package 'controller'
2. created file 'controller/author.py'
3. moved the following from main.py to 'controller/author.py':
   1. AuthorRepository
   2. provide_authors_repo
   3. provide_author_details_repo
   4. AuthorController
## refactor to extract the model related parts into model files ###
1. created Python package 'model'
2. created file 'model/author.py'
3. moved the following from main.py to 'model/author.py':
   1. AuthorModel
   2. Author
   3. AuthorCreate
   4. AuthorUpdate
4. created file 'model/book.py'
5. moved the following from main.py to 'model/book.py':
   1. BookModel
## refactor to extract common/shared elements into their own file ###
1. created 'common.py'
2. moved BaseModel from main.py to 'common.py'

OpenAPI site can be accessed via:
   - http://localhost:8000/schema
   - http://localhost:8000/schema/swagger
   - http://localhost:8000/schema/elements
   - http://localhost:8000/schema/redoc
   - http://localhost:8000/schema/rapidoc