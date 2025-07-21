FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY src/ ./src/

RUN pip3 install -r requirements.txt

# Set environment variables for config/cache dirs to avoid permission errors
ENV HOME=/app
ENV MPLCONFIGDIR=/app/.config/matplotlib

RUN mkdir -p /app/.streamlit /app/.config/matplotlib

# Add non-root user (recommended)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8501

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    HF_HOME=/app/huggingface

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
