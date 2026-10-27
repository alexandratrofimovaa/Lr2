import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data) #разбор текста
dom.normalize()

elements = dom.getElementsByTagName('Valute')
Valute_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    num_code = int(child.firstChild.data)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    char_code = child.firstChild.data
    Valute_dict[num_code] = char_code #создание словаря

print(Valute_dict)