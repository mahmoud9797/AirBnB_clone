#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = Amenity()
my_user.Amenity = "toliet"
my_user.save()
print(my_user)
