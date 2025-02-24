mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


freeze:
	pip freeze > requirements.txt


admin:
	python3 manage.py createsuperuser


make udb:
	rm -rf db.sqlite3
	rm -rf authentication/migrations/*
	touch authentication/migrations/__init__.py
	rm -rf expense/migrations/*
	touch expense/migrations/__init__.py
	python3 manage.py makemigrations
	python3 manage.py migrate