import xml.etree.ElementTree as ET

def serialize_to_xml(sample_dict, filename):
    """serialize xml"""
    try:
        root = ET.Element("data")
        for key, value in sample_dict.items():
            child = ET.SubElement(root, str(key))
            child.text = "" if value is None else str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False
    
def deserialize_from_xml(xml_file):
    """deserialize xml"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text if child.text is not None else ""
        return result
    except Exception:
        return None