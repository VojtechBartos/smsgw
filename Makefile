
default:
	docker-compose up

dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

stop:
	docker-compose stop
