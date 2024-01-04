pipenv install
pipenv shell

python seed.py
python app.py


pipenv run test
pipenv run coverage
