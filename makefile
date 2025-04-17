start:
	python manage.py runserver $(port)

migrations:
	python manage.py makemigrations $(app_name)

migrate:
	python manage.py migrate $(app_name)

startapp:
	python manage.py startapp $(app_name)

shell:
	python manage.py shell

superuser:
	python manage.py createsuperuserz

css:
	npx @tailwindcss/cli -i ./static/css/project-input.css -o ./static/css/project.css --watch

format:
	npx prettier --write $(file)
