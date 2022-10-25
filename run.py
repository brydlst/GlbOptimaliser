# Python App to compress and repack GLTB files
# import Python modules
import os
import json

# -- try to install requests module if not present
try:
    import easygui
    import gltflib
except ImportError:
    os.system('pip install easygui')
    os.system('pip install gltflib')
# -- if all went well, import required module again (for global access)
import imageio.v3 as iio
import easygui as g
from gltflib import GLTF

# varriables
imgID = 0 # Do NOT touch this, its used to store the position of found jpgs in gltf
JpgQuality = 50 # Controls the compression quality. Value from 0 - 100. Default is 50

# Open file dialog
OpenFile = g.fileopenbox(title='Select GLTF file to repack',default='*.gltf',filetypes=["*.gltf"])

if OpenFile == None:
    quit()
print("Selected File:")
print(OpenFile)
print("")

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
print("Compressing with Jpg quality: ", JpgQuality, "/ 100")
print("Searching for images to edit...")
for string in data['images']:
    search_and_rewrite("baseColor")
    search_and_rewrite("occlusionRoughnessMetallic")
    search_and_rewrite("emissive")
    imgID = imgID + 1


# Save edited Json to GLTF file
JsonData = json.dumps(data, ensure_ascii=False, indent=4)
with open(OpenFile, "w") as File:
    File.write(JsonData)
    
# repack gltf to glb 
gltf = GLTF.load(OpenFile)
SaveFileGlb = OpenFile[:-4] +"glb"
gltf.export(SaveFileGlb)
print("All Done")

wait = input("Press Enter to Exit")