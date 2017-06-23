import json
from collections import OrderedDict


id2name = json.loads(open("id2name.json", "r", encoding="utf8").read())

f = open("result.json", "w",encoding="utf8")

name2id = OrderedDict({})

for i in id2name:
    name2id[id2name[i]] = i


json.dump(name2id,f,ensure_ascii=False)