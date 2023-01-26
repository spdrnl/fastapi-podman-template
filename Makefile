VERSION := $(shell poetry run python -c 'import tomli; print(tomli.load(open("pyproject.toml", "rb"))["tool"]["poetry"]["version"])')


run-integration: stop-container remove-run-container build-run-container run-container sleep call stop-container
	echo "Done."

run-container:  
	podman container run -d --name fastai-podman -p 8000:80 --network bridge fastai-podman

stop-container:
	podman stop -i fastai-podman

build-run-container:
	podman image build -t fastai-podman .

remove-run-container: 
	podman container rm -i fastai-podman

sleep:
	sleep .1

run-local:
	poetry run uvicorn app.rest.server:app --reload

dev-install:
	poetry install

call:
	http localhost:8000

test-local:
	poetry run pytest tests/


run-test-container: remove-test-container build-test-container run-test-container

remove-test-container:
	podman container rm -i fastai-podman-test

build-test-container: 
	podman image build -f Dockerfile-test -t fastai-podman-test .

run-test-container: 
	podman container run --name fastai-podman-test fastai-podman-test

create-docs:
	rm -rf site 
	poetry run mkdocs build

