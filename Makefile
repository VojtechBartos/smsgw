default:
	docker-compose up -d

dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

stop:
	docker-compose stop

deploy:
	(cd provisioning/; ansible-playbook machine.yml)
