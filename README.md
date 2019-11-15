# demopypackage1
A simple demo to show how to create a Python package for PyPI

***
# Purpose of this package
This package together with its homepage on GitHub explains how to create a Python package for the Python package index PyPI.
The package includes a (dead) simple program, not a library, and that is on purpose.

# How to install this package
This package is not available on PyPI, instead it is available simply for education purposes here on test.pypi.org.

To install the package:
First, create a virtual environment for Python:
e.g. via Anaconda or pip.
Then:

`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple demopypackage1d`

# How to run the program
In a terminal window with the newly created virtual environment:  
`python -m demopypackage1`

or e.g.   

`python -m demopypackage1 --param1 0 --param2 0`

The program does very little indeed, as little as possible (just some arithmetic), as the functionality of the program is not the main point here.

# Creating and testing installation of a package
## Summary of steps to create a package
Here a summary of the steps to create such a package.
1. We create an account on GitHub
2. We create a new GitHub repo under a given organisation on GitHub. The repo name is *demopypackage1*.
3. We create this repo with selections made for the files .gitignore and LICENSE.
4. Next we clone the nearly empty repo into a local project folder *lpf*. This creates a local folder *lpf/demopypackage1*.
5. Next we create a folder structure within *lpf/demopypackage1* as is available on GitHub (see homepage). To stay on top of the structure and its content, displaying the structure with `$ tree` in a terminal window is helpful.
6. Now time to name the package purely for how it shall show up on PyPI. The name is used for pip install.
This name must be unique on PiPY. We have chosen: demopypackage1x with x = e. For previous versions, we used x = a, b, ...
7. Of course, as the modules in the package should perform some work, we need to create some code. For the purpose here, the code is kept very very simple.
See the project homepage on GitHub.
Our repo name (locally within the *lpf*) is: *demopypackage1*.
To make things a bit more interesting, we include:
	- a main package in the repo folder: demopypackage1
	- a subpackage within demopypackage1
	- non-Python files like config.text
	- a package tests that is not to be imported.  
The main package and its subpackage are to be imported.
The main script is called \__main\__.py.
8. Now we create a file requirements.txt. This can be used by other developers who would fork your package and would like to install the exact package versions you used for development of your package software.   
From the Python environment:  
`$ pip freeze > requirements.txt`
9. We set the version in the \__init\__.py and setup.py files:  	
`__version__ = "1.0.0"` or any other version.
10. Next we create the (rather important) setup.py file (see this project's homepage on GitHub for details).
11. Now time to create the README.md markdown file, i.e. this text. This can be elegantly done using Atom.
12. To define which other non-Python files we want to include into the package, we write a manifest file: MANIFEST.in.
13. Commit the code to the local git repo master and push to GitHub.
14. Install twine with    
`$ pip install twine`
15. Create a source code archive and a wheel for the package from the folder that holds setup.py:  
Cd into the folder that holds setup.py: demopypackage1.   
`$ python setup.py sdist bdist_wheel`
16. Check whether the package has been correctly created from folder dist:  
`$ cd dist`    
`$ tar tzf demopypackage1d-1.0.1.tar.gz`    
Check whether all files are included, including e.g. important non-Python files like config.txt.
17. Run a check with twine:     
`$ cd ..`    
Then run from outside folder dist:      
`$ twine check dist/*`
18. Register an account at test.pypi.org to test your package.
19. Upload the package from your local computer to TestPyPI:  
cd to the folder that includes the dist folder:   
`$ twine upload --repository-url https://test.pypi.org/legacy/ dist/* `
20. If the upload is successful, go to test.pypi.org and check your project there.


## How to test installation of the package
1. Create a test Python environment using e.g. Anaconda, conda or pip.
2. Start a new terminal window.
3. Activate the test environment
4. Install the package from the test.pypi.org site:   
`$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple demopypackage1d`

    > Above is important as in the case of this demopypackage1, some packages need to be installed from PyPI itself.

5. Once the package is successfully installed, try to run the program.    
`$ python -m demopypackage1`
6. Deactivate the test environment.
7. Remove the test environment.   
DONE.

Finally:
1. Push the final version of your local repo to GitHub.
2. Publish the final package (if it does a great job) on PyPI.
***
## URLs used for above:   
Guide to the Markdown syntax:    https://www.markdownguide.org/basic-syntax

PyPI site:
https://pypi.org

Test PyPI site:
https://test.pypi.org

Packaging Pyton projects
https://packaging.python.org/tutorials/packaging-projects/

> We have reached the end!

***
[Link to the project's GitHub page](https://github.com/YUCtechlab/demopypackage1)

Created: 2019 Nov 15
