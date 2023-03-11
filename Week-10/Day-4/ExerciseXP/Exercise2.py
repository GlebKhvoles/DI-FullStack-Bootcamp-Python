
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

open_sampleJson = json.loads(sampleJson)
print(open_sampleJson['company']['employee']['payable']['salary'])
open_sampleJson['company']['employee']['birth_date'] = '1995-09-04'
with open('sampleJson.json', 'w') as j:
	json.dump(open_sampleJson, j, indent = 5)