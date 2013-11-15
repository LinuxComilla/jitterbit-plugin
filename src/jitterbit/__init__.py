from lxml import etree
from lxml.builder import E

__author__ = 'Jussi Talaskivi'


class plugin:
    def __init__(self):
        self.input_files = []
        self.output_files = {}
        self.data_elements = []
        self.parse_input_xml()

    def parse_input_xml(self):
        inputxml = etree.parse("input.xml")
        self.input_files = [tag.values()[0] for tag in inputxml.findall(".//File[@Name]")]
        self.output_files = dict([inputfile, None] for inputfile in self.input_files)
        for tag in inputxml.findall(".//DataElement"):
            dataelement = dict(tag.items())
            dataelement.update({"Value":tag.text})
            self.data_elements.append(dataelement)

    def generate_output_xml(self):
        outputxml = E.JitterbitPlugin(E.PipelinePluginOutput(E.Files, SpecVersion="1.0"), SpecVersion="1.0")
        filesxml = outputxml.find("PipelinePluginOutput").find("Files")
        for outputfile in self.output_files:
            target = self.output_files[outputfile] or outputfile
            filexml = E.File(E.Origin(E.File(Name=outputfile)),Name=target)
            filesxml.append(filexml)
        output = etree.tostring(outputxml, encoding="utf-8", pretty_print=True, xml_declaration=True)
        f = open("output.xml", "w")
        f.write(output)
        f.close()
