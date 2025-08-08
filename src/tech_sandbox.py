from optparse import Values
import json, os

mydict_1 = {"Name": "template",
                         "IDnumber": "0001",
                         "RelatedEvents": ["0002","0003","0004"],
                         "Version": "01",
                         "ViewOrder": "01",
                         "BodyText": "Lorem ipsum....."}

mydict_2 = {"Name": "templat2",
                         "IDnumber": "0002",
                         "RelatedEvents": ["0001","0003","0004"],
                         "Version": "01",
                         "ViewOrder": "02",
                         "BodyText": "Lorem ipsum.....2"}

mydict_3 = {"Name": "templat2",
                         "IDnumber": "0002",
                         "RelatedEvents": ["0001","0003","0004"],
                         "Version": "01",
                         "ViewOrder": "02",
                         "BodyText": "Lorem ipsum.....2"}

dict_dict = {"0001":mydict_1, "0003":mydict_2,"0002":mydict_3}

lv_values = dict_dict.pop("0001")
print(lv_values)

dict_dict.update({"0004":lv_values})
print(dict_dict.keys())
#dict_dict.pop

#print(dict_dict['0002'])



#filepath = os.getcwd() + "/data/eventdata.json"

#with open(filepath, mode="w", encoding="utf-8") as write_file:
#    json.dump(dict_dict, write_file,indent=2,sort_keys=True)

#with open(filepath, mode="r",encoding="utf-8") as read_file:
#    read_data:dict = json.load(read_file)

#set_list_id = list(read_data.keys())

#int_list = list(map(int, set_list_id))

#print(int_list)
