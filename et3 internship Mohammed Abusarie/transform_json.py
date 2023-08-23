import json

#getting the scale factor
old_data=[0.432857 ,0.190476 ,0.0971429 ,0.213333]
new_data=[38.428555, 8.38095 ,9.71429 ,21.3333]
factors=[]

for i in range(len(old_data)):
    factors.append( new_data[i]/old_data[i] )

#creating our json template
jsonvar=dict()
jsonvar["annotations"]=[{
    "result":[]
}]


file_path="image1.txt"
with open(file_path, 'r') as file:
    for line in file:
        li=line.strip().split(" ")
        float_list = [float(item) for item in li]
        print(float_list)
        jsonvar["annotations"][0]["result"].append(
            {
                "image_rotation": 0,
                "value": {
                    "x": float_list[1]*factors[0],
                    "y": float_list[2]*factors[1],
                    "width": float_list[3]*factors[2],
                    "height": float_list[4]*factors[3],
                    "rotation": 0,
                    "rectanglelabels": [
                        "object"
                    ]
                }
            }
        )

# Write the dictionary to a JSON file
with open("output.json", 'w') as json_file:
    json.dump(jsonvar, json_file)