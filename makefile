start:
	python manage.py runserver $(port)

migrations:
	python manage.py migrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

superuser:
	python manage.py createsuperuser

css:
	npx @tailwindcss/cli -i ./static/css/project-input.css -o ./static/css/project.css --watch

format:
	npx prettier --write $(file)
