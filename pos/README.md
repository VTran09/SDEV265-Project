# Change the directory to where the repository is stored in

# Setup terminal and pip
python -m pip install --upgrade pip setuptools virtualenv

# Create your local virtual environment
python -m virtualenv kivy_venv

# Activate the virtual environment on Windows
kivy_venv\Scripts\activate

# Install Kivy
python -m pip install "kivy[full]" kivy_examples

# Checking the demo
python kivy_venv\share\kivy-examples\demo\showcase\main.py

# Try running the hello.py file
python hello.py

# Note: You might get underlined error messages when importing kivy. It is normal as long as running the main program in the virtual environment.

# Deactivate the virtual environment
deactivate
```