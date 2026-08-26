#Dictionary (make use of{})

info={ "Name": "Pranita",
      "collage": "S.I.E.S",
      "cgpa": 99.99}

print(info)
print(info["Name"])# Be careful about[] brackrts in dict
print(type(info))
# Dictionary are mutable
info["cgpa"]=100
print(info)
print(len(info))

