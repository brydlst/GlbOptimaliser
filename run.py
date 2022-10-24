# Python App to compress and repack GLTB files
# import Python modules
import os
import json
import imageio.v3 as iio
import easygui as g
from gltflib import GLTF

# varriables
imgID = 0
JpgQuality = 50

# Open file dialog
OpenFile = g.fileopenbox(title='Select GLTF file to repack',default='*.gltf',filetypes=["*.gltf"])

if OpenFile == None:
    quit()
print(OpenFile)

# Load GLTB as Json file
with open(OpenFile, "r") as File:
    data = json.load(File)

# Functions -----------------------------------------
def search_and_rewrite(search_for):
    if search_for in string["uri"]:
        
        file_name = string["uri"]
#       print(file_name)
        file_name_ed = file_name[:-3] + "jpg"
#       Convert png file_name to jpg
        im = iio.imread(os.path.dirname(OpenFile) + "/" + file_name)
        iio.imwrite(os.path.dirname(OpenFile) + "/" + file_name_ed, im, quality=JpgQuality)
        print(file_name_ed)
        
        data['images'][imgID]['uri'] = file_name_ed    
# Functions -----------------------------------------

# Check GLTF json for png images    
print("Jpg quality: ", JpgQuality)
print("Searching for images to edit...")
for string in data['images']:
    search_and_rewrite("baseColor")
    search_and_rewrite("occlusionRoughnessMetallic")
    search_and_rewrite("emissive")
    imgID = imgID + 1
else:
    print("Done")

# Save edited Json to GLTF file
JsonData = json.dumps(data, ensure_ascii=False, indent=4)
with open(OpenFile, "w") as File:
    File.write(JsonData)
    
# repack gltf to glb 
gltf = GLTF.load(OpenFile)
SaveFileGlb = OpenFile[:-4] +"glb"
gltf.export(SaveFileGlb)