run: 
	podman container run -d --name fastapi-podman -p 8000:80 --network bridge fastapi-podman

run-dev:
	poetry run uvicorn app.main:app --reload

dev:
	poetry install

container:
	podman image build -t fastapi-podman .
