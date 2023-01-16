FROM python:3-slim as python
ENV PYTHONUNBUFFERED=true
WORKDIR /work


FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-interaction --no-ansi -vvv



FROM python as runtime
ENV PATH="/work/.venv/bin:$PATH"
COPY --from=poetry /work /work
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
