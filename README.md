# ldproxy service yml generator

A simple python script for creating basic structure for the service configuration file(`store/entities/services`) for [ldproxy](https://github.com/interactive-instruments/ldproxy). Script also generates structure for some api buildingblocks

Currently the following building blocks are supported

- `QUERYABLES`
- `TILES`
- `CRS`
- `STYLES`

Edit the specific values for CRS and TILES manually after config file has been created.

### Running the code in Ubuntu

1.  create a virtual environment `python3 -m venv venv`
2.  activate environemnt `source venv/bin/activate`
3.  install packages `pip install -r requirements.txt`
4.  rename `config_example.py` to `config.py` and edit the connection string
5.  manually set the `id` to whatever id you need
6.  manually edit `api_buildingblocks` list by adding or removing api buildings blocks from the list
7.  Run the script to create the yml configuration file for a service
