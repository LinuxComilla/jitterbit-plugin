from lxml import etree
from lxml.builder import E

__author__ = 'Jussi Talaskivi'


class Plugin:
    def __init__(self):
        self.input_files = []
        self.output_files = {}
        self.data_elements = []
        self.parse_input_xml()

    def parse_input_xml(self):
        input_xml = etree.parse("input.xml")
        self.input_files = [tag.values()[0] for tag in input_xml.findall(".//File[@Name]")]
        self.output_files = dict([input_file, None] for input_file in self.input_files)
        for tag in input_xml.findall(".//DataElement"):
            data_element = dict(tag.items())
            data_element.update({"Value":tag.text})
            self.data_elements.append(data_element)

    def generate_output_xml(self):
        output_xml = E.JitterbitPlugin(E.PipelinePluginOutput(E.Files, SpecVersion="1.0"), SpecVersion="1.0")
        files_xml = output_xml.find("PipelinePluginOutput").find("Files")
        for output_file in self.output_files:
            target = self.output_files[output_file] or output_file
            file_xml = E.File(E.Origin(E.File(Name=output_file)),Name=target)
            files_xml.append(file_xml)
        output = etree.tostring(output_xml, encoding="utf-8", pretty_print=True, xml_declaration=True)
        f = open("output.xml", "w")
        f.write(output)
        f.close()
