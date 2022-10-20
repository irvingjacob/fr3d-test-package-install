# Installing fr3d-python with pip install from TestPyPI

- In order for fr3d-python to have full functionality straight from the pip install, you must be running python in version 3.6 and above. 
- `config.py`, `environment.yml`, and `requirements.txt` are all provided in this repository. 

## Installing Using Anaconda 
- I recommend testing with an Anaconda Environment with python 3.8.
	- I've provided a .yml file that will create an anaconda environment with most everything you will need called `fr3d-test-install`
	- This environment can be created by running  `conda env create -f environment.yml`
	- Switch to this environment using `conda activate fr3d-test-install`
		- Since fr3d is only on testPyPI, I can't include it in the yml file. 
		- Install fr3d from testPyPI by running  `python -m pip install --index-url https://test.pypi.org/simple/ --no-deps fr3d`
## Installing Locally
- If you don't have anaconda or want to just install it on your base, you can simply run `python -m pip install --index-url https://test.pypi.org/simple/ --no-deps fr3d`
	- You may need to install its dependencies. 
	- I've created a requirements.txt you can use to install dependencies
	-  ` pip install -r requirements.txt`
	- Or `pip install matplotlib mmcif-pdbx numpy scipy` to do it manually 
## Optional setup to use installed fr3d package
- In order to use fr3d-python without specifying input and output paths every time you run, you can create a file called config.py that specifies which directories input and output should be ran.
	- Below is an outline of how we recommended to setup your config.py file and local file structure to use FR3D-Python. This directory contains my version of this config.py which you can edit to reflect your own file structure.

 ```
config = {}
config['3d_structure_file_path'] = 'C:/Users/User/.../FR3D/PDBFiles/' 
config['annotation_text_path'] = 'C:/Users/User/.../FR3D/NAPairwiseInteractions/'
config['unit_data_binary_path'] = 'C:/Users/User/.../FR3D/Python FR3D/data/units/' 
config['unit_annotation_binary_path'] =
'C:/Users/User/.../FR3D/Python FR3D/data/units/'
config['pairwise_annotation_binary_path'] = 'C:/Users/User/.../FR3D/Python FR3D/data/pairs/'
config['fr3d_search_html_path'] = 'C:/Users/User/.../FR3D/fr3d_search_html_pages/' #HTML documents
config['diagnostic_html_path'] = 'C:/Users/User/.../FR3D/html_pages/' #HTML documents
```
- Below is how I would recommend setting up your file structure to work to specify input and output of certain files using fr3d-python
```
FR3D
|  
└─── config.py 
│
└───3DStructureFiles
|   |    
|   └─── Where .cif or .pdb Files will be stored or downloaded to 
└───AnnotationTextOutput
|   │  
|   └───Text
|   |   |
|   |   └─── Where .txt files of annotations will be output 
|   |
|   └───Binary
|   |   |
|   |   └─── Where binary files or .pickle files will be output 
└───PythonFR3D
|   |
|   └───data
|       |
|       └───pairs
|
└───FR3DSearchHTMLPages
|
└───DiagnosticHTMLPages
```

## Using Installed fr3d package
If you have installed fr3d-python and have navigated to the folder where config.py is, you can use the following commands (If you did not set up config.py, you will need to use -i and -o flags when running these commands, otherwise the programs will create folders or download files to the working directory):

## Problems
If anyone uses this and encounters any issues, please email jimitch@bgsu.edu and I will work at resolving these issues.