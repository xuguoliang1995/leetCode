# import pandas as pd
#
# df = pd.read_table(''null'.txt')
#
# df.drop_duplicates(inplace=True)
# print(df)
# df.to_csv('new_'null'.txt',index=False)



# import pymongo
# import json
# client = pymongo.MongoClient('localhost',27017)
# db = client.immunology
# collection = db.coll
# datas = collection.find()
# count = 0
# d_list = []
# for data in datas:
#     d = {}
#     d['link'] = data['link']
#     d['issn'] = data['issn']
#     d['if_2017'] = data['if_2017']
#     d['source'] = data['source']
#     d_list.append(d)
#     print(data['link'])
#     print(data['issn'])
#     print(data['if_2017'])
#     print(data['source'])
#     count += 1
# print(count)
# d_json = json.dumps(d_list)
# with open('Map.txt', 'w',encoding='utf-8') as fp:
#      fp.write(d_json + '\n')






"""
['1476-4687', '1546-1696', '1546-1718', '2058-5276', 
'2041-1723', '1476-4679', '1529-2916', '1546-170X', 
'1748-3395', '1546-1726', '1476-4660', '1759-5010', 
'1759-4782', '1474-1768', '1476-5551']
"""

import json
# a = [
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0354-1",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0301-1",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4138",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0151-7",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0155-3",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0154-4",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0153-5",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0136-4",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0164-2",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0180-0",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0185-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0188-5",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0197-4",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0182-y",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05418-8",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0178-7",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05577-8",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0125-0",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0618-482",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4170",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0154-7",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0134-y",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0131-1",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0158-3",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0088-5",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0175-2",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0161-8",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0201-4",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0168-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0167-2",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0184-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0197-y",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-017-0062-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0086-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0068-6",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0088-2",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0085-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0087-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0105-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0099-z",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0123-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0122-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0107-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0142-0",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0134-0",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0140-2",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0146-9",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0159-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0157-6",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0158-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0176-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0178-1",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0177-2",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0190-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0200-7",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0196-z",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0199-9",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0161-x",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0167-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0171-8",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0186-1",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0162-9",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0173-6",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0175-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0174-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0180-7",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0185-2",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0183-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0182-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0179-0",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0184-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0202-5",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0201-6",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0188-z",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0192-3",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0194-1",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0187-0",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0189-y",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0191-4",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0198-x",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0178-z",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0186-z",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0181-4",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0190-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0185-0",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0179-y",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0197-9",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0188-x",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0189-9",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0183-2",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0225-9",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0200-5",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0192-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0204-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0194-z",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0207-y",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0195-y",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0202-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0208-x",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0205-0",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41593-018-0181-6",
#         "issn":"1546-1726",
#         "if_2017":19.912,
#         "source":"Nature neuroscience"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0247-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0177-0",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0174-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0164-5",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0176-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0173-4",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0166-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0191-2",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0170-7",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0147-6",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0182-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0211-2",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0206-z",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0199-7",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0184-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0213-0",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0215-y",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0212-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0214-z",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0220-1",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0210-3",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0187-y",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0218-8",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0198-8",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0094-7",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0087-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0090-y",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0083-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0103-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0096-5",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0089-4",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0102-y",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0095-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0092-9",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0081-z",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0133-4",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0093-8",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0106-7",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41565-018-0180-5",
#         "issn":"1748-3395",
#         "if_2017":37.49,
#         "source":"Nature nanotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0115-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0116-5",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0101-z",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0125-4",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0091-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0124-5",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0105-8",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0117-4",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0132-5",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0131-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0133-z",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0136-9",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0135-x",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0130-2",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0129-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0120-4",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0128-9",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-017-0024-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0140-0",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0137-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0139-6",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0144-9",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0155-6",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0157-4",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0156-5",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0162-7",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0145-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0161-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0160-9",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0159-2",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4177",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0163-6",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4175",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-563b",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-565",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4163",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-561",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-559b",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-557",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4190",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4186",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4178",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4176",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4174",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-563a",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-559a",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-562",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4193",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-560",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4191",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4187",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4185",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4207",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0127-y",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0131-2",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0133-0",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0124-1",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0163-7",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0132-1",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0141-0",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0136-x",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0164-6",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0101-8",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0166-4",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0140-1",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0144-x",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0138-8",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0147-7",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4188",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0143-y",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0165-5",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0145-9",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0151-y",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0142-z",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0146-8",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0155-7",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0148-6",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0108-3",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0105-6",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0104-7",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0107-4",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0106-5",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0101-x",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0109-2",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41556-018-0122-3",
#         "issn":"1476-4679",
#         "if_2017":19.064,
#         "source":"Nature cell biology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0110-9",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0112-7",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0123-4",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0116-3",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0120-7",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0118-1",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0130-5",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0145-y",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0134-1",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0141-2",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0133-2",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0128-z",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0135-0",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0132-3",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0138-x",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0136-z",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0144-z",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05563-0",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05247-9",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05544-3",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05426-8",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05520-x",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05589-4",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05525-6",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05518-5",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05478-w",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05461-5",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05327-w",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05586-7",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05581-y",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05553-2",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05322-1",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05510-z",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05475-z",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05574-x",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05527-4",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05503-y",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05531-8",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05496-8",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41467-018-05555-0",
#         "issn":"2041-1723",
#         "if_2017":12.353,
#         "source":"Nature communications"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41563-018-0137-y",
#         "issn":"1476-4660",
#         "if_2017":'null',
#         "source":'null'
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0177-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0195-6",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0196-5",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0187-6",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0198-3",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0190-y",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0203-x",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0200-0",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0191-x",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0192-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0205-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0210-y",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0189-4",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0209-4",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0213-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0215-6",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0204-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0140-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0149-z",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0154-2",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0158-y",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0143-5",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0153-3",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0152-4",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0169-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0172-0",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0173-z",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0170-2",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0175-x",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0168-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0181-z",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0193-8",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0186-7",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0206-7",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0202-y",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0208-5",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0212-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0211-x",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0194-7",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0207-6",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0199-2",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0123-y",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41564-018-0220-9",
#         "issn":"2058-5276",
#         "if_2017":14.174,
#         "source":"Nature microbiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0161-5",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0156-2",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0165-1",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0157-1",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0159-z",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0166-0",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0170-4",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0168-y",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0160-6",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0169-x",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0175-z",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0147-3",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0176-y",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0173-1",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0158-0",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0171-3",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0182-0",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4147",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4140",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4172",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4153",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4154",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4150",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4151",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4166",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4152",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4162",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4194",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4173",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-660d",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-660b",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-660c",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt0718-660a",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4181",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4184",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4182",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4179",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4183",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0167-z",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4192",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41588-018-0174-0",
#         "issn":"1546-1718",
#         "if_2017":27.125,
#         "source":"Nature genetics"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4180",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/nbt.4199",
#         "issn":"1546-1696",
#         "if_2017":35.724,
#         "source":"Nature biotechnology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0347-0",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0335-4",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0405-7",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0391-9",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0385-7",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0378-6",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0334-5",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0394-6",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0374-x",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0387-5",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0384-8",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0396-4",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0377-7",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0371-0",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0389-3",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0393-7",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0386-6",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0366-x",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0367-9",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0361-2",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0403-9",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0382-x",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41586-018-0358-x",
#         "issn":"1476-4687",
#         "if_2017":41.577,
#         "source":"Nature"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0150-y",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0143-x",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0166-3",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0168-1",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0167-2",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0169-0",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0172-5",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0165-4",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0174-3",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0171-6",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0164-5",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0122-2",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0066-y",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0066-0",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0071-6",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0042-3",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0044-1",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0046-z",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0047-y",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0049-9",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0023-6",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0024-5",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0030-7",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0034-3",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0037-0",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0038-z",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0076-1",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0078-z",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0077-0",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0172-3",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0179-9",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0175-0",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0107-z",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0129-6",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0035-y",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0034-z",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0010-7",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0016-1",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0038-8",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0017-0",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0040-1",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0106-0",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0058-4",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0061-9",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0029-9",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0051-y",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41568-018-0043-2",
#         "issn":"1474-1768",
#         "if_2017":42.784,
#         "source":"Nature reviews. Cancer"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41375-018-0168-z",
#         "issn":"1476-5551",
#         "if_2017":10.023,
#         "source":"Leukemia"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0079-y",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0080-5",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0036-9",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0046-7",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0058-3",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0055-6",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0074-3",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0073-4",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0037-8",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0026-y",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0070-4",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0069-x",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0071-3",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0068-y",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0072-2",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0046-4",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0049-1",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0052-6",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0059-z",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0061-5",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0075-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41569-018-0064-2",
#         "issn":"1759-5010",
#         "if_2017":1.714,
#         "source":"Nature reviews. Cardiology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0076-9",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0069-8",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0074-y",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0080-0",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0079-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0067-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0123-6",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0120-9",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0109-4",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0113-8",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0122-7",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0127-2",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0118-3",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0111-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0112-9",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0121-8",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0114-7",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0126-3",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0110-y",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0119-2",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0148-x",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0149-9",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0115-1",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0117-z",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0142-y",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0141-z",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0153-8",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0149-4",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0146-7",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0151-x",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41591-018-0072-0",
#         "issn":"1546-170X",
#         "if_2017":32.621,
#         "source":"Nature medicine"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0147-6",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0173-4",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0170-7",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0175-2",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41590-018-0148-5",
#         "issn":"1529-2916",
#         "if_2017":21.809,
#         "source":"Nature immunology"
#     },
#     {
#         "link":"https://www.nature.com/articles/s41571-018-0075-2",
#         "issn":"1759-4782",
#         "if_2017":3.055,
#         "source":"Nature reviews. Clinical oncology"
#     }
# ]
# L = []
# for i in a:
#     if i['issn'] not in L:
#        L.append(i['issn'])
#        L.append(i)
# json_str = json.dumps(L)
# with open('simple_Map.txt','w',encoding='utf-8') as f:
#     f.write(json_str)



