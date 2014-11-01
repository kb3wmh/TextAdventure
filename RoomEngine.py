#Room Engine

import xml.etree.ElementTree as ET
tree = ET.parse('adventure.xml')
root = tree.getroot()

rooms = root.findall("Room")