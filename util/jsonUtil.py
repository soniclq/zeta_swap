import json


class jsonUtil:

 @classmethod
 def load_json(self,path):
  with open(path,'r',encoding='utf8') as fp:
     return json.load(fp)
