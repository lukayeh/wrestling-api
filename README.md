# Getting started

Start the api using: `sh run.sh`

# Using the api

Get all wrestlers:
```
curl http://127.0.0.1:8000/wrestler
```

Search wrestler by name:
```
curl http://127.0.0.1:8000/wrestler\?name\=Jon%20Moxley
```

Add wrestler using curl:
```
curl -X POST http://0.0.0.0:5000/wrestler \
   -H 'Content-Type: application/json' \
   -d '{
  "name": "Mangey Jeff",
  "billFrom": "Chelsmford, United Kingdom",
  "signatureMoves": [
    "Dodgy Knee"
  ],
  "finishingMoves": [
    "Mange maker"
  ],
  "dob": "20/03/1991",
  "works_for": "Free Agent",
  "birthName": "Jeff Mange",
  "nickNames": [
    "The Mangey one"
  ]
}'

```

*note:* `%20` is to replace a `space`

# Playing with the db

run: `docker run -p 8000:8000 -d amazon/dynamodb-local`

create table and populate:
```
python3 generate_table
```

Validate table has been created:
```
export AWS_ACCESS_KEY_ID=example
DYNAMO_ENDPOINT=http://localhost:8000 dynamodb-admin
```