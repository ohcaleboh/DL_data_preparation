
# The purpose of this script is to automate the creation of a specific number of directories w/ specfic name

# Import os module
import os

# Parent Directory Path
root_path = '/Users/caleboh/Desktop/Liver_seg/liver_seg/dicom_file/labels'

# Create the directories in your list at the path specified for each item
for item in range(131): 
    new_item = str(item)
    item_1 = f"liver_{new_item}"
    path = os.path.join(root_path, item_1)
    os.mkdir(path)
    print("Directory '% s' created" % item_1)






  







