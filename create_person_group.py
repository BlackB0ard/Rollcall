import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = '17122c4be3214178ab93127fad066013'
CF.Key.set(Key)

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print(personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print(res)
