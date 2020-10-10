
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse(r'C:\Users\19608\Desktop\test.xml')
tree1 = DOMTree.documentElement
list1 = tree1.getElementsByTagName("user")
# print(list1[0].getElementsByTagName("password")[0].childNodes[0].data)
print(list1[0].getElementsByTagName("password")[0])