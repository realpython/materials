FROM python:3.14-slim

WORKDIR /app
COPY ./src/ /app

COPY ./pyproject.toml /code/pyproject.toml
RUN python -m pip install /code/.

EXPOSE 8000
CMD ["sh", "entrypoint.sh"]
