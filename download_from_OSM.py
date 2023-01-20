import requests as r


def main():
    api = 'http://www.overpass-api.de/api/interpreter'
    cities = {
        '北京市': 912940,
        '长沙市': 3202711,
        '长春市': 2763992,
        '成都市': 2110264,
        '重庆市': 913069,
        '福州市': 3263977,
        '广州市': 3287346,
        '贵阳市': 2782246,
        '哈尔滨市': 2755608,
        '海口市': 2784613,
        '杭州市': 3221112,
        '合肥市': 3288965,
        '呼和浩特市': 2752851,
        '济南市': 3486449,
        '昆明市': 2723597,
        '拉萨市': 2745046,
        '兰州市': 2701949,
        '南昌市': 3169865,
        '南京市': 2131524,
        '南宁市': 2775778,
        '上海市': 913067,
        '沈阳市': 2769604,
        '石家庄市': 3009732,
        '太原市': 3296588,
        '天津市': 912999,
        '乌鲁木齐市': 2752472,
        '武汉市': 3076268,
        '西安市': 3226004,
        '西宁市': 2707990,
        '银川市': 3307138,
        '郑州市': 3283765,
    }
    data = '''
[maxsize:300000000][timeout:1800];
way(area:{})->.a;
(
    way.a[highway=trunk];
    way.a[highway=primary];
    way.a[highway=secondary];
    way.a[highway=tertiary];
    way.a[highway=residential];
    way.a[highway=unclassified];
)->.b;
way.b[~"^name(:zh)?$"~"."];
out tags noids;
    '''

    for city_name, relation_id in cities.items():
        data = data.format(3600000000+relation_id)
        s = r.session()
        _ = s.post(api, data=data).text
        with open(f'osm\\{city_name}.xml', 'w', encoding='utf8') as f:
            f.write(_)


if __name__ == '__main__':
    main()
