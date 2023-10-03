import time
from yamlmaker import generate
from api_buildingblocks import Queryables, Tiles, Styles, CRS

class Service:
    def __init__(self, id:str, table_names:list, api_buildingblocks:list):
        self.config = {
            "id": id,
            "createdAt": round(time.time()),
            "lastModified": round(time.time()),
            "entityStorageVersion": 2,
            "label": id,
            "description": "",
            "enabled": True,
            "serviceType": "OGC_API",
            "api": [],
            "collections": {}
        }

        self.create_api_buildingblocks(api_buildingblocks)
        self.create_collections(table_names)   

    def create_api_buildingblocks(self, api_buildingblocks:list):
        
        for api in api_buildingblocks:

            if (api == 'QUERYABLES'):
                self.config["api"].append(Queryables().export_as_dict())

            if (api == 'TILES'):
                self.config["api"].append(Tiles().export_as_dict())

            if (api == 'CRS'):
                self.config["api"].append(CRS().export_as_dict())
                
            if (api == 'STYLES'):
                self.config["api"].append(Styles().export_as_dict())
           

    def create_collections(self, table_names):
        for table_name in table_names:
            self.config["collections"][table_name] = {"id": table_name, "label": table_name, "enabled": True}

   
    def create_yaml(self):
        generate(self.config)

    
