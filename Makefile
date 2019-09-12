export PORT=5000
export APP_NAME=qa_task

build: ## Build the container
	docker build -t $(APP_NAME) .

run: ## Run container
	docker run -d -p $(PORT):$(PORT) --name="$(APP_NAME)" $(APP_NAME)

up: build run ## Build and run container

down: ## Stop and remove a running container
	docker stop $(APP_NAME); docker rm $(APP_NAME)

test: ## Run tests
	docker exec -it $(APP_NAME) pytest tests --port $(PORT)