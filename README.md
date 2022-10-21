

# wrestling-api

<p align="center">
<a href="https://sonarcloud.io/summary/overall?id=lukayeh_wrestling-api">
<img alt="Quality Gate Status" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=alert_status">
<img alt="Duplicated Lines (%)" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=duplicated_lines_density">
<img alt="Reliability Rating" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=reliability_rating">
<img alt="Technical Debt" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=sqale_index">
<img alt="Lines of Code" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=ncloc">
<img alt="Code Smells" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=code_smells">
<img alt="Maintainability Rating" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=sqale_rating">
<img alt="Security Rating" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=security_rating">
<img alt="Bugs" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=bugs">
<img alt="Vulnerabilities" src="https://sonarcloud.io/api/project_badges/measure?project=lukayeh_wrestling-api&metric=vulnerabilities">
</a>
<img alt="Python 3.9" src="https://img.shields.io/badge/python-3.9-blue">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

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