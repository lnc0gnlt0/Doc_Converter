import os
import Parser


def parse(path, encoding):
    files = []
    out_files = []

    for el in Parser.XmlParser.from_file(path).data.getroot().iter():
        _, _, tag = el.tag.rpartition('}')
        if tag == 'Compile':
            if 'Include' in el.attrib:
                file = el.attrib["Include"]\
                    .replace('\\\\', '/')\
                    .replace('\\', '/')
                files.append(f'{os.path.split(path)[0]}/{file}')

    for file_path in files:
        _, extension = os.path.splitext(file_path)
        if extension == '.cs':
            out_files.extend(
                Parser.CsParser.parse(file_path, encoding)
            )

    return out_files
