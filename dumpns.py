import xml.etree.ElementTree as ET

TITLE = "{http://www.imsglobal.org/xsd/imsccv1p2/imscp_v1p1}title"

tree = ET.parse("manifest.xml")
# tree = ET.parse("test2.xml")
root = tree.getroot()

# returns just the directory structure
org = tree.findall(".//{*}organizations/{*}organization/")
org = org[0][0]
# root_dir == logical root directory we care about
root_dir = org


def show_tree(elementtree, depth=0):
  for thing in elementtree:
    spacer = '|'
    if thing.find(TITLE) is not None:
      current_thing = thing.find(TITLE).text
      for i in range(depth):
        spacer = spacer + '-'
      if 'identifierref' in thing.keys():
        # only files have an identifierref
        # print(spacer, thing.get('identifierref'), os.listdir(thing.get('identifierref'))[0])
        print(spacer, thing.get('identifierref'), current_thing)
      else:
        print(spacer, current_thing)
    else:
      depth += 1
    show_tree(thing, depth)

show_tree(org)
