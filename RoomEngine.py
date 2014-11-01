#Room Engine

#import xml file
import xml.etree.ElementTree as ET
tree = ET.parse('adventure.xml')
root = tree.getroot()

rooms = root.findall("room")

print rooms