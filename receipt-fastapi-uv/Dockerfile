# Fast, neat uv-based image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen

COPY app ./app

ENV DATA_DIR=/data
VOLUME ["/data"]
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
