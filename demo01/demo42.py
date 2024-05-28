try:
    import xml.etree.cElementTree as ET
except Exception as e:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='infor.xml')
root = tree.getroot()

for user in root:
    # print(user)
    print(user[1].tag)
    print(user[0].text, user[1].text)