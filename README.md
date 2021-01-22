<!-- Recomendo a consulta: https://docs.github.com/pt/github/writing-on-github/basic-writing-and-formatting-syntax -->
<!-- E esse também: https://medium.com/@raullesteves/github-como-fazer-um-readme-md-bonit%C3%A3o-c85c8f154f8 -->

# Kitchin Kanri

## Description

> **_Important_**: all requests with body must be sent as JSON format;

> **_Important_**: when Authorization Headers is needed, must be sent as Bearer;

## Base url:

Use this URL as base to requests:

> `https://kitchin-kanri.herokuapp.com`

## Endpoints:

### POST /orders

- don't need authentication
> #### request body:
>
>```
> {
>	"payment_method": "dinheiro",
>	"products": [13, 8]
> }
>```

- **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "message": "Successfully created"
> }
>```

### DELETE /orders/<int:order_id>

- need authentication

- **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "message": "Ok"
> }
>```

- **If something went wrong:** http status code: 422
> #### response body:
>
>```
> {
>  "msg": "Signature verification failed"
> }
>```
### GET /orders

- need authentication

- **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "data": [
>     {
>       "date": "2021-01-22T00:37:26.042902",
>       "id": 1,
>       "payment_method": "dinheiro",
>       "products": [
>         {
>           "category_id": 7,
>           "description": "Tempura",
>           "id": 13,
>           "image": "tempura.png",
>           "name": "Tempura",
>           "price": 5.5
>         },
>       {
>           "category_id": 6,
>           "description": "Sashimi",
>           "id": 8,
>           "image": "sashimi.png",
>           "name": "Sashimi",
>           "price": 5.5
>         }
>       ],
>       "status": "Pedido pendente",
>       "total_price": 11.0
>     },
>     {
>       "date": "2021-01-22T00:38:41.640979",
>       "id": 2,
>       "payment_method": "dinheiro",
>       "products": [],
>       "status": "Pedido pendente",
>       "total_price": 0.0
>     }
>   ]
> }
>```

- **If something went wrong:** http status code: 422
> #### response body:
>
>```
> {
>   "msg": "Bad Authorization header. Expected value > 'Bearer <JWT>'"
> }
>```


### GET /orders/<int:order_id>

- don't need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "date": "2021-01-22T00:37:26.042902",
>     "id": 1,
>     "payment_method": "dinheiro",
>     "products": [
>       {
>         "category_id": 7,
>         "description": "Tempura",
>         "id": 13,
>         "image": "tempura.png",
>         "name": "Tempura",
>         "price": 5.5
>       },
>       {
>         "category_id": 6,
>         "description": "Sashimi",
>         "id": 8,
>         "image": "sashimi.png",
>         "name": "Sashimi",
>         "price": 5.5
>       }
>     ],
>     "status": "Pedido pendente",
>     "total_price": 11.0
>   }
> }
> ```

- **If something went wrong:** http status code: 404
> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```

### PUT /orders/<int:order_id>

- need authentication

{
	"status": "Pedido Andamento"
}
#### request body:
> 
>```
> {
> 	"status": "Pedido Andamento"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "date": "2021-01-22T00:37:26.042902",
>     "id": 1,
>     "payment_method": "dinheiro",
>     "products": [
>       {
>         "category_id": 7,
>         "description": "Tempura",
>         "id": 13,
>         "image": "tempura.png",
>         "name": "Tempura",
>         "price": 5.5
>       },
>       {
>         "category_id": 6,
>         "description": "Sashimi",
>         "id": 8,
>         "image": "sashimi.png",
>         "name": "Sashimi",
>         "price": 5.5
>       }
>     ],
>     "status": "Pedido Andamento",
>     "total_price": 11.0
>   }
> }
> ```

- **If something went wrong:** http status code: 404
> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```

### POST /products

- need authentication
> #### request body:
>
>```
> {
> 	"name": "example",
> 	"price": 4.25,
> 	"description": "exampl example",
> 	"category_id": 1,
> 	"image": "image.png"
> }
>```

- **If everything goes right:** http status code: 201
> #### response body:
>
>```
> {
>   "message": "Successfully created"
> }
>```

- **If something went wrong:** http status code: 422

> #### response body:
>
>```
> {
>   "msg": "Signature verification failed"
> }
>```

### DELETE /products/<int:product_id>

- need authentication

- **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "message": "Ok"
> }
>```


- **If something went wrong:** http status code: 422
> #### response body:
>
>```
> {
>   "msg": "Signature verification failed"
> }
>```


### GET /products

- don't need authentication

- **If everything goes right:** http status code: 200
> #### response body:
>
> ```
> {
>   "data": [
>     {
>       "category_id": 1,
>       "description": "example1",
>       "id": 1,
>       "name": "example example1",
>       "price": 5.5
>     },
>     {
>       "category_id": 2,
>       "description": "example2",
>       "id": 1,
>       "name": "example example2",
>      "price": 6.25
>     }
>   ]
> }
> ```


### GET /products/<int:product_id>

- don't need authentication

- **If everything goes right:** http status code: 200
> #### response body:
>
>```
> {
>   "data": {
>     "category_id": 1,
>     "description": "example",
>     "id": 1,
>     "name": "example example",
>     "price": 6.75
>   }
> }
>```

- **If not found:** http status code: 404

> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```

### PUT /products/<int:product_id>

- need authentication
> #### request body (how element you need update):
>
> ```
> {
>   "name": "new_name"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "category_id": 1,
>     "description": "example",
>     "id": 25,
>     "name": "new_name",
>     "price": 4.25
>   }
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "msg": "Signature verification failed"
> }
> ```

### DELETE /users/<int:id_user>

- need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "message": "Ok"
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```

### GET /users/<int:id_user>

- need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "email": "henrique@gmail.com",
>     "id": 5,
>     "is_admin": true,
>     "name": "Henrique"
>   }
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```
### PATCH /users/<int:id_user>

- need authentication
> #### request body (how element you need update):
>
> ```
> {
> 	"email": "querbrincarnaneve@gmail.com"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "email": "querbrincarnaneve@gmail.com",
>     "id": 14,
>     "is_admin": true,
>     "name": "Jhon Snow"
>   }
> }
> ```

- **If something went wrong:** http status code: 404
> #### response body:
>
> ```
> {
>   "message": "Not found"
> }
> ```
### GET /users

- need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": [
>     {
>       "email": "im_the_queen@gmail.com",
>       "id": 1,
>       "is_admin": true,
>       "name": "Rainha Elizabeth"
>     },
>     {
>       "email": "im_the_king@gmail.com",
>       "id": 2,
>       "is_admin": true,
>       "name": "Rei Charles"
>     },
>     {
>       "email": "brunocampos@hotmail.com",
>       "id": 8,
>       "is_admin": true,
>       "name": "Bruno"
>     },
>     {
>       "email": "williane@gmail.com",
>       "id": 9,
>       "is_admin": true,
>       "name": "willian"
>     },
>     {
>       "email": "snowland@gmail.com",
>       "id": 7,
>       "is_admin": true,
>       "name": "Jhon Snow"
>     },
>     {
>       "email": "terradegela@gmail.com",
>       "id": 14,
>       "is_admin": true,
>       "name": "Jhon Snow"
>     }
>   ]
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   'data': []
> }
> ```

### POST /auth/login

- need authentication
> #### request body (how element you need update):
>
> ```
> {
> 	"email": "jinjeiro@hotmail.com",
> 	"password": "1234"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "data": {
>     "access_token": > "eyJ0eXAiOiJKV1QiL",
>     "email": "terradegela@gmail.com",
>     "fresh_token": > "AmDvD2zAGAV9SXcOfv1l3BqU",
>     "is_admin": true,
>     "name": "Jhon Snow"
>   }
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "message": "Unauthorized"
> }
> ```

### POST /auth/signup

- don't need authentication

> #### request body:
>
> ```
> {
>     "name": "example",
>     "email": "test@email.com,
>     "password": "password",
>     "is_admin": true OR false,
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>     "message": "created"
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>     "message": "User e-mail already in use"
> }
> ```

### GET /categories

- need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> [
>   {
>     "id": 1,
>     "name": "Sobremesas"
>   },
>   {
>     "id": 2,
>     "name": "Bebidas"
>   },
>   {
>     "id": 3,
>     "name": "Comidas Frias"
>   },
>   {
>     "id": 4,
>     "name": "Comidas Quentes"
>   },
>   {
>     "id": 5,
>     "name": "Pratos Quentes"
>   }
> ]
> ```

### POST /categories

- need authentication
> #### request body (how element you need update):
>
> ```
> {
> 	"name": "Sobremesas",
> 	"image": "sobremesas.png"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
> 	"name": "Sobremesas",
> 	"image": "sobremesas.png"
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "msg": "Signature verification failed"
> }
> ```

### DELETE /categories/<int:category_id>

- need authentication

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "message": "Deleted"
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "msg": "Signature verification failed"
> }
> ```
### PATCH /categories/<int:category_id>

- need authentication
> #### request body (how element you need update):
>
> ```
> {
> 	"name": "Pratos frios"
> }
> ```

- **If everything goes right:** http status code: 200

> #### response body:
>
> ```
> {
>   "id": 6,
>   "name": "Pratos frios"
> }
> ```

- **If something went wrong:** http status code: 422
> #### response body:
>
> ```
> {
>   "msg": "Signature verification failed"
> }
> ```