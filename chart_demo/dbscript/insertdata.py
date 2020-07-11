import django
import os
import json
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chart_demo.settings")
django.setup()

with open('../static_files/H04.txt', 'r', encoding="UTF-8") as f:
    data = f.read()
data = data.replace("'", '"')
data = data.replace("id", 'b_id')
data = data.replace(r"\n", '')
data = data.replace(r"\\", '')

res = re.findall(r"{[^{]+}", data)

from dbdata.serializer import ChartInfoSerializer

num = 0
for i in res:
    dic_text = json.loads(i)
    chat = ChartInfoSerializer(data=dic_text)
    if chat.is_valid():
        chat.save()
        num += 1
    else:
        print(chat.errors)
print(num)
