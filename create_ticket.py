import os 
import json
from glpi import GLPI

url = os.getenv("GLPI_API_URL") or None
user = os.getenv("GLPI_USERNAME") or None
password = os.getenv("GLPI_PASSWORD") or None
token = os.getenv("GLPI_APP_TOKEN") or None

glpi = GLPI(url, token, (user, password))

print("Pegando todos os tickets")

glpi_out = glpi.get_all('ticket')

print(glpi_out)

"""
glpi_out = json.dumps(glpi.get_all('ticket'),
                  indent=4,
                  separators=(',', ': '),
                  sort_keys=True)
"""

glpi.kill()