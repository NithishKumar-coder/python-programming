import json
with open ("all_entities.json","w") as f:
 def Get_Entity(label):
        entity=label
        name=get(entity)
        if len(name)!=0:
            print({"Entity":entity,"Name_list ": name})
            with open ("all_entities.json","a") as f:
                f.write(json.dumps({"Entity":entity,"Name_list":name}, sort_keys=False, indent=2, separators=(',', ': '))) 

 
 def get(entity):
    entity=entity
    name_list=[]
    with open("Data.json") as f:
        data=json.load(f)
        for items in data:
            if entity==items['Entity']:
                name_list.append(items['Name'])
    
    return name_list
