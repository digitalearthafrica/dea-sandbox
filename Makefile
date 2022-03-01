help: ## Print this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## Build the default sudo image using Docker Compose
	docker-compose -f docker-compose.yml -f docker-compose.override.yaml build

up:  ## Start up an environment with a database
	docker-compose up

shell:
	docker-compose run sandbox bash

up-k8s:  ## Start up an environment without a database
	docker-compose -f docker-compose.yml up

clean:
	docker-compose down --rmi all -v
