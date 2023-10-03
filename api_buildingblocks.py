class Queryables():
    def __init__(self):
        self.config = {
            "buildingBlock": "QUERYABLES",
            "enabled": True
        }

    def export_as_dict(self):
        return self.config

class Tiles:
    def __init__(self):
        self.config = {
            "BuildingBlock": "TILES",
            "enabled": True,
            "tileProvider": {
                "type": "FEATURES",
                "zoomLevels": {
                "WebMercatorQuad": {
                    "min": 3,
                    "max": 15
                }},
            "seeding": {
                "WebMercatorQuad": {
                    "min": 3,
                    "max": 15
                }},
            "multiCollectionEnabled": True         
            },
            "cache": "MBTILES"
        }

    def export_as_dict(self):
        return self.config
    
class CRS: 
    def __init__(self):
        self.config = {
            "BuildingBlock": "CRS",
            "enabled": True,
            "additionalCrs": [{"code": 25832, "forceAxisOrder": "NONE"},
                              {"code": 4258, "forceAxisOrder": "NONE"},
                              {"code": 3857, "forceAxisOrder": "NONE"}]
        }
    
    def export_as_dict(self):
        return self.config
  
class Styles:
    def __init__(self):
        self.config = {
            "BuildingBlock": "STYLES",
            "enabled": True,
            "deriveCollectionStyles": True
        }
    def export_as_dict(self):
        return self.config
