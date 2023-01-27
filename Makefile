VERSION := $(shell cat pyproject.toml | grep -m1 version | grep -P "([\d+\.]*)" -o)


run-integration: run-container sleep call stop-container
	echo "Done."

run-container: stop-container remove-run-container build-run-container 
	podman container run -d --name fpt -p 8000:80 --network bridge fpt

stop-container:
	podman stop -i fpt

build-run-container:
	podman image build -t fpt .

remove-run-container: 
	podman container rm -i fpt

sleep:
	sleep .1

run-server:
	poetry run uvicorn fpt.rest.server:app --reload

run-command:
	poetry run hello world

dev-install:
	poetry install

call:
	http localhost:8000

test-local:
	poetry run pytest tests/


run-test-container: remove-test-container build-test-container run-test-container

remove-test-container:
	podman container rm -i fpt-test

build-test-container: 
	podman image build -f Dockerfile-test -t fpt-test .

run-test-container: 
	podman container run --name fpt-test fpt-test

create-docs:
	rm -rf site 
	poetry run mkdocs build

format:
	poetry run black .
	poetry run flake8 .
