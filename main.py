from fastapi import FastAPI
from influxdb_client import InfluxDBClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your React frontend (replace with your frontend URL)
origins = ["http://localhost:3000"]  # Add your frontend URL here

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

token = "PNnMUu2JqpF8MdrpqQsg2ofZvnRvi0UfNGcMi62tTlNi6o-APZKHMzM7XKEJnHl--iNspWJywHrQo9A_6rCO7Q=="
org = "IoT"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"
bucket = "IoT"

client = InfluxDBClient(url=host, token=token, org=org)

@app.get("/")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''

    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []   

    for table in tables:
        for record in table.records:
            data_point = {
                "time": record.values["_time"],
            }

            # Mapping the liquidTemp and other fields to their corresponding values
            for field_name in ["humidity", "liquidTemp", "rainValue", "soilMoistureValue", "temperature"]:
                if record.values["_field"] == field_name:
                    data_point[field_name] = record.values["_value"]

            # Add additional fixed keys and values
            data_point["device"] = "ESP32"

            data.append(data_point)

    return {"data": data}

@app.get("/humidity")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''
    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []
    
    for table in tables:
        for record in table.records:
            # Mapping the liquidTemp and other fields to their corresponding values 
            if record.values["_field"] ==  "humidity":
                data.append([record.values["_time"], record.values["_value"]])

    return {"data": data}

@app.get("/liquidtemp")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''
    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []
    
    for table in tables:
        for record in table.records:
            # Mapping the liquidTemp and other fields to their corresponding values 
            if record.values["_field"] ==  "liquidTemp":
                data.append([record.values["_time"], record.values["_value"]])

    return {"data": data}

@app.get("/rainValue")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''
    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []
    
    for table in tables:
        for record in table.records:
            # Mapping the rainValue and other fields to their corresponding values 
            if record.values["_field"] ==  "rainValue":
                data.append([record.values["_time"], record.values["_value"]])

    return {"data": data}

@app.get("/soilMoistureValue")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''
    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []
    
    for table in tables:
        for record in table.records:
            # Mapping the soilMoistureValue and other fields to their corresponding values 
            if record.values["_field"] ==  "soilMoistureValue":
                data.append([record.values["_time"], record.values["_value"]])

    return {"data": data}

@app.get("/temperature")
async def get_data():
    query = '''
        from(bucket: "IoT")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "sensor_data")
    '''
    # Execute the query
    tables = client.query_api().query(org=org, query=query)

    data = []
    
    for table in tables:
        for record in table.records:
            # Mapping the temperature and other fields to their corresponding values 
            if record.values["_field"] ==  "temperature":
                data.append([record.values["_time"], record.values["_value"]])

    return {"data": data}