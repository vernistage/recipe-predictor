# recipe-predictor

Clone this repository onto your computer and cd into the directory

Install a virtual environment for your dependencies
python3 -m venv myvenv

Activate your local environment
source myenv/bin/activate

Make sure you have the latest pip installed
python3 -m pip install --upgrade pip

Install project requirements
pip install -r requirements.txt

Start up the database
python manage.py migrate

Boot-up app on your local server
python manage.py runserver
