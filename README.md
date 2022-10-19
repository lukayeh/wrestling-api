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

