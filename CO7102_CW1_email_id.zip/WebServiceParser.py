import xml.etree.ElementTree as ET
import json
#mysourcepath and mytargetpath
source_path = r'C:\\Users\\Jeeva\\OneDrive\\Documents\\test\\WebServiceProvider.xml'
outputnew_json = r'C:\\Users\\Jeeva\\OneDrive\\Documents\\WebServiceProvider.json'
#getting the root of the element
Source_parse = ET.parse(source_path)
master_file = Source_parse.getroot()
#fetching the header method
result_output = {"abstract_method": []}
#gathering the methodname and visibility and arguments
for newmethod in master_file.findall('abstract_method'):
    method_info = {
        "method_name": newmethod.get("name"),
        "visibility": newmethod.find("visibility").text if newmethod.find("visibility") is not None else None,
        "arguments": {
            "parameter": [
                {
                    "datatype": param.get("type"),
                    "label": param.text
                }
                for param in newmethod.find("arguments").findall("parameter")
            ] if newmethod.find("arguments") is not None else []
        }
    }
   #fetching the available exceptions 
    exceptions = [exc.text for exc in newmethod.find("exceptions").findall("exception")] if newmethod.find("exceptions") is not None else []
    if exceptions:
        method_info["exceptions"] = {"exception": exceptions}
    #method Return
    method_info["return"] = newmethod.find("return").text if newmethod.find("return") is not None else None
    result_output["abstract_method"].append(method_info)
#storing the output
with open(outputnew_json, 'w') as f:
    json.dump(result_output, f, indent=4)
#printing the output in json
print(f"JSON output has been saved to {outputnew_json}")
