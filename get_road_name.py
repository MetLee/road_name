import json
import os
import re


def main():
    file_names = os.listdir('osm')
    xml_file_names = []
    for file_name in file_names:
        if file_name.split('.')[-1] == 'xml':
            xml_file_names.append('osm\\'+file_name)

    road_names = set()
    for file_name in xml_file_names:
        with open(file_name, 'r', encoding='utf8') as f:
            data = f.read()

        _road_names = set()
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)[东|南|西|北|中]?[一|二|三|四|五|六|七|八|九|十]?[大]?街"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)[东|南|西|北|中]?[一|二|三|四|五|六|七|八|九|十]?巷"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)[东|南|西|北|中]?[一|二|三|四|五|六|七|八|九|十]?弄"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)[东|南|西|北|中]?[支]?[一|二|三|四|五|六|七|八|九|十]?[公|高架|辅]?路"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)大道"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W]{2,}?)胡同"/>', data)
        _road_names |= set(_)
        _ = re.findall(r'<tag k="name(?:\:zh)?" v="([^\W][东|南|西|北|中])[街|路]"/>', data)
        _road_names |= set(_)

        road_names |= _road_names

    with open('road_names.txt', 'w', encoding='utf8') as f:
        for road_name in road_names:
            f.write(road_name + '\n')

    with open('docs\\road_names.json', 'w', encoding='utf8') as f:
        json.dump(list(road_names), f, ensure_ascii=False)


if __name__ == '__main__':
    main()
