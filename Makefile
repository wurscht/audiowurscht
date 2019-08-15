.PHONY: docker start

docker: ## Start the docker environment
	@docker-compose up

start: ## Start the development server
	python manage.py runserver