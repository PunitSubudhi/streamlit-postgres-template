FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PYTHONPATH=/app

COPY pyproject.toml uv.lock .python-version ./

RUN uv pip install --no-cache --system -r pyproject.toml

COPY . .

CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]