import ast
import csv
file1 = open("C:/Users/ADMIN/AppData/Local/Programs/Python/Python37/resultyoutube.txt","r",encoding='utf-8')
json1_str = file1.read()
#print(json1_str)
json1_data = ast.literal_eval(json1_str)
#json1_data = json.loads(json1_str)
#print(json1_data)
csv_file = "C:/Users/ADMIN/AppData/Local/Programs/Python/Python37/resultyoutube.csv"

column_names = ['channel_id']
for key2,value2 in json1_data.items():
    for key, value in value2.items() :
    #    print (key) 
        if(len(value) == 1 ) :
            dict = {'chnnel_id':key}
            for key1, value1 in value[0].items() :
                dict.update({key1:value1})
                if(key1 not in column_names):
                    column_names.append(key1)
#            print(dict)
#    print(column_names)        
try:
    with open(csv_file, 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()
        for key2,value2 in json1_data.items():
            for key, value in value2.items() :
                if(len(value) == 1 ) :
                    dict = {'channel_id':key}
                    for key1, value1 in value[0].items() :
                        dict.update({key1:value1})
                    writer.writerow(dict)
except IOError:
    print("I/O error") 
    
file1.close()
