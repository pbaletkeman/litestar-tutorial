1. added `OpenAPIControllerExtra` to main.py to specify favicon for OpenAPI interfaces
2. added `openapi_config=OpenAPIConfig`:
   1. added title and version
   2. set default OpenAPI to spotlight elements
   3. set OpenAPI path to `/docs`
   4. turn off create examples by default
   5. connect `OpenAPIControllerExtra`
   6. tell OpenAPI where to get endpoint description from
3. configure path for non Python assets, multiple locations can be used.

### litestar --app step2.main:app run ###

### OpenAPI site can be accessed via: ###
   - http://localhost:8000/docs
   - http://localhost:8000/docs/swagger
   - http://localhost:8000/docs/elements
   - http://localhost:8000/docs/redoc
   - http://localhost:8000/docs/rapidoc