# Getting started

Start the api using: `sh run.sh`

# Using the api

Get all wrestlers:
```
curl http://127.0.0.1:8000/wrestler
```

Get wrestler by id:
```
curl http://127.0.0.1:8000/wrestler?id=1
```

Search wrestler by name:
```
curl http://127.0.0.1:8000/wrestler\?name\=Jon%20Moxley
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