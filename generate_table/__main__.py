import boto3
import json


def initialize_db():
    ddb = boto3.resource(
        "dynamodb",
        endpoint_url="http://localhost:8000",
        region_name="us-east-1",
        aws_access_key_id="example",
        aws_secret_access_key="example",
    )

    return ddb


def generate_wrestlers(ddb):
    ddb.create_table(
        TableName="wrestlers",
        AttributeDefinitions=[{"AttributeName": "name", "AttributeType": "S"}],
        KeySchema=[{"AttributeName": "name", "KeyType": "HASH"}],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    print("Successfully created table wrestlers")


def drop_wrestlers(ddb):
    table = ddb.Table("wrestlers")
    table.delete()


def generate_table():
    ddb = initialize_db()
    generate_wrestlers(ddb)


def drop_table():
    ddb = initialize_db()
    try:
        drop_wrestlers(ddb)
    except:
        print("Unable to drop table")
        pass


def populate_table():
    ddb = initialize_db()
    table = ddb.Table("wrestlers")
    try:
        with open("data/wrestlers.json") as json_data:
            wrestlers = json.load(json_data)

            with table.batch_writer() as batch:

                # Loop through the JSON objects
                for wrestler in wrestlers:
                    # print(wrestler)
                    batch.put_item(Item=wrestler)
        print("Successfully populated table wrestlers")
    except:
        print("Failed to populate table wrestlers")


if __name__ == "__main__":
    drop_table()
    generate_table()
    populate_table()
