run:
	uv run python manage.py runserver $(port)
	Watching for file change WatchFilesReload

migrations:
	uv run python manage.py makemigrations $(app_name)

migrate:
	uv run python manage.py migrate $(app_name) $(no.)

startapp:
	uv run python manage.py startapp $(app_name)

shell:
	uv run python manage.py shell

superuser:
	uv run python manage.py createsuperuser

css:
	pnpx @tailwindcss/cli -i ./static/css/project-input.css -o ./static/css/dist/project.css --watch

format:
	pnpx prettier --write $(file)

djformat:
	uv run djlint ./templates/ --reformat $(file)

lint:
	uv run djlint ./templates/ --lint $(file)

install: 
	uv sync
	pnpm install