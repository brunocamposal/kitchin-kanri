<!-- Recomendo a consulta: https://docs.github.com/pt/github/writing-on-github/basic-writing-and-formatting-syntax -->
<!-- E esse também: https://medium.com/@raullesteves/github-como-fazer-um-readme-md-bonit%C3%A3o-c85c8f154f8 -->

# Kitchin Kanri

## Description

> **_Important_**: all requests with body must be sent as JSON format;

> **_Important_**: when Authorization Headers is needed, must be sent as Bearer;

## Base url:

Use this URL as base to requests:

> `https://api..../ `

## Endpoints:

### POST /orders

- não precisa login
- acrescentar o que precisa para fazer a requisição
- mostrar o que virá como resposta

### DELETE /orders/<int:order_id>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /orders

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /orders/<int:order_id>

- não precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### PUT /orders/<int:order_id>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### POST /products

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### DELETE /products/<int:product_id>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /products

- não precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /products/<int:product_id>

- não precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### PUT /products/<int:product_id>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### DELETE, GET, PATCH /users/<int:id_user>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /users

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### GET /authentication/fresh_token

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### POST /authentication/login

- não precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### POST /authentication/signup

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

- **If everything goes rigth:** http status code: 200

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

### GET, POST /categories

- precisa login no POST
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta

### DELETE, PATCH /categories/<int:category_id>

- precisa login
- especificar o que precisa constar no corpo da requisação
- mostrar o que virá como resposta
