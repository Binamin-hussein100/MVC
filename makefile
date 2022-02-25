serve:
	python3 manage.py runserver

migrate:
	python3 manage.py migrate

check:
	python3 manage.py check

migrations:
	python manage.py makemigrations

shell:
	python manage.py shell

virtual:
	pipenv shell

user:
	python manage.py createsuperuser

cached:
	git rm --cached <file name>