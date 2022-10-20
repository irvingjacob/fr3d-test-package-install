# add variables specific to your machine

#3d_structure_file_path -> location locally where 3D structure files will be located or downloaded to 
#annotation_text_path -> location where output of a text file with annotations or relevent output will be placed
#unit_data_binary_path -> location of binary or pickle files for unit data
#unit_annotation_binary_path -> location whre output of binary or pickle files will be placed 

# Edit below path to be representative of your local file structure
config = {}
config['3d_structure_file_path'] = 'C:/Users/jmitc/Documents/FR3D/PDBFiles/' #This is the same as -i or --input 
config['annotation_text_path'] = 'C:/Users/jmitc/Documents/FR3D/NAPairwiseInteractions/' #NA_Pairwise_Interactions, NA_unit_annotation, NA_protein_annotation
config['unit_data_binary_path'] = 'C:/Users/jmitc/Documents/FR3D/Python FR3D/data/units/' # could be the same or different path as 'unit_annotation_binary_path
config['unit_annotation_binary_path'] = 'C:/Users/jmitc/Documents/FR3D/Python FR3D/data/units/' # could be the same or different path as unit_data_binary_path
config['pairwise_annotation_binary_path'] = 'C:/Users/jmitc/Documents/FR3D/Python FR3D/data/pairs/' #Windows users enable case sensitive file names here
config['fr3d_search_html_path'] = 'C:/Users/jmitc/Documents/FR3D/fr3d_search_html_pages/' #HTML documents
config['diagnostic_html_path'] = 'C:/Users/jmitc/Documents/FR3D/html_pages/' #HTML documents

#Old definition of localpath
# inputPath = 'C:/Users/jmitc/Documents/FR3D/PDBFiles/'
# outputNAPairwiseInteractions = 'C:/Users/jmitc/Documents/FR3D/NAPairwiseInteractions/'
# outputText = 'C:/Users/jmitc/Documents/FR3D/RNAProtein/proteinRNA_%s.txt' # Reroute to 'annotation_text_path'
# outputBaseAAFG = 'C:/Users/jmitc/Documents/FR3D/RNAProtein/aa-fg_base_%s.csv' # Reroute to 'annotation_text_path'
# outputNAPickleInteractions = 'C:/Users/jmitc/Documents/FR3D/Python FR3D/data/pairs/' # Reroute to 'pairwise_annotation_binary_path'
# contact_list_file = 'C:/Users/jmitc/Documents/FR3D/RNAProtein/contact_list_%s.txt' # Reroute to 'annotation_text_path' 
# outputHTML = 'C:/Users/jmitc/Documents/FR3D/RNAProtein/output' # Reroute to 'diagnostic_html_path'
# storeMatlabFR3DPairs = "C:/Users/jmitc/Documents/FR3D/Python FR3D/data/pairs/"

