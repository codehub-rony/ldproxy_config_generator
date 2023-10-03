import config 
from sqlalchemy import create_engine, inspect
from services import Service

# connect to database
try:
    engine = create_engine(config.postgres_connection_string)
    insp = inspect(engine)

except Exception as e:
    print("Error connecting to PostgreSQL:", str(e))

# set input parameters
# id: id of service
# list of api blocks. Currently supported: "QUERYABLES", "TILES", "CRS", "STYLES"
id = "test"
api_buildingblocks = ["QUERYABLES", "TILES", "CRS", "STYLES"]

service_yaml = Service(id, insp.get_table_names(), api_buildingblocks)

service_yaml.create_yaml()

engine.dispose()

