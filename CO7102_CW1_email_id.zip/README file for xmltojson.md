
README for XML to JSON Converter:

Overview:
This Python script is designed to convert an XML file containing information about abstract methods into a JSON format. The script reads the XML structure, extracts relevant details about each abstract method, and then saves this data as a JSON file.

Requirements:
--> Python 3.x
--> The xml.etree.ElementTree and json modules (these are part of the standard Python library, so no additional installation is needed).

Input File:
--> The script expects an XML file named WebServiceProvider.xml. The file path should be specified in the source_path variable.

How It Works:
--> Parse the XML: The script uses the ElementTree module to parse the XML file specified in source_path.
--> Extract Method Information: It iterates through each <abstract_method> element to collect:
        The method name (from the name attribute)
        Visibility (from the <visibility> tag)
        Arguments (from the <arguments> tag and its <parameter> elements)
        Exceptions (from the <exceptions> tag and its <exception> elements, if present)
        Return type (from the <return> tag)
--> Store Data in a Dictionary: All collected information is stored in a Python dictionary structured for JSON output.
--> Save as JSON: Finally, the script saves the dictionary to a JSON file specified in the output_json variable.

Output File:
--> The output will be a JSON file named WebServiceProvider.json, saved in the path specified in the output_json variable. The JSON will be formatted for readability.

How to Run:
--> Ensure that your XML file is correctly structured and located at the path specified in the source_path variable.
--> Update the output_json variable if you want to change the output file location or name.
--> Run the script using Python.

Run the script using Python:
--> python WebServiceParser.py

