setup:
	@make build
	@make up
build:
	docker compose up -d --build --force-recreate beeru
down:
	docker compose down
rebuild:
	docker compose up -d --build --force-recreate
stop:
	docker compose stop
up:
	docker compose up -d
