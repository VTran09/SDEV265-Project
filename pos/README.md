# 1. Install pip package
python -m pip install --upgrade pip setuptools virtualenv

# 2. Create your local virtual environment
python -m virtualenv kivy_venv

# 3. Activate the virtual environment before running the app
kivy_venv\Scripts\activate (for Windows)

# 4. Install Kivy
python -m pip install "kivy[full]" kivy_examples

