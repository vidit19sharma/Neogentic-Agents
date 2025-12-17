# Neogentic-Agents
This is my Army of Agents

## Setup

### 1. Enviorment Variables
    1. create a .env file and paste the neccessary API keys in it
    2. for Gemini API Key put use variable : "GEMINI_API_KEY"
    3. for Weather API key use variable : OPEN_WEATHER_API_KEY for understanding and how it works refer to weather.py 

### 2. Virtual Enviorment
  A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

#### 1. Create a virtual environment
    
    python -m venv myenv

#### 2. Activate the virtual environment (Linux/macOS)
    
    source myenv/bin/activate

#### 3. Activate the virtual environment (Windows)

    myenv\Scripts\activate.bat

#### 4. Deactivate the virtual environment
    deactivate

### 3. Installation ("requirements.txt")
In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:
    
#### Output the list of installed packages and their versions to a file
    pip freeze > requirements.txt

#### Install the packages listed in the requirements.txt file

    pip install -r requirements.txt

