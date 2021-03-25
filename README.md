# Python-Selenium-Framework
Setup : 

Create and manage a virtual environment : 
  
  1. **Create a Virtual environment (venv)** : This step is to generate an environment specific to the project you are working on. Below are the steps in creating a virtual environment
      1. **Installing virtual environment** -> _python3 -m pip install --user virtualenv_
      2. **Creating virtual environment** -> _python3 -m venv env_
      3. **Activate the virtual environment** -> _source env/bin/activate_
  
  2. **Setup the virtual environment** : In order to set up the virtual environment to satisfy the package dependencies, navigate to the Shared folder and run the following command in your shell
      
      _pip install -r requirements.txt_
      
  3. **Executing the specific test file in the repository** : Now that we have the virtual environment created and set up for the project, we are ready to execute any or all individual test files present in the repository. There are a couple of ways in which we can do this as below 
  
      1. **Run a particular file** : _pytest -v -s /path/to/test_file.py_
      2. **Run all files in the repo** : _pytest -v -s_ 
