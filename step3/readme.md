1. Added ***put*** method to author controller<br>
   **PATCH** is used to apply partial updates to a resource, meaning that only the fields that need to be changed are sent in the request body.<br>
   **PUT** is used to replace the entire resource with a new representation, meaning that all the fields of the resource are sent in the request body, even if they are not modified.
2. Cleanup some code by removing commented out code
 
### litestar --app step3.main:app run ###

### OpenAPI site can be accessed via: ###
   - http://localhost:8000/docs
   - http://localhost:8000/docs/swagger
   - http://localhost:8000/docs/elements
   - http://localhost:8000/docs/redoc
   - http://localhost:8000/docs/rapidoc