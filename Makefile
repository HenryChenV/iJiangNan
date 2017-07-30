server:
	python manage.py runserver

shell:
	python manage.py shell

dbshell:
	python manage.py dbshell

deploy:
	git pull && python manage.py collectstatic && touch ~/softwares/uwsgi/apps-enabled/iJiangNan.ini
