server:
	python manage.py runserver

shell:
	python manage.py shell

dbshell:
	python manage.py dbshell

deploy:
	python manage.py collectstatic
