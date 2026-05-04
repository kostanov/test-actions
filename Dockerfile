FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml main.py ./

# Install dependencies using uv
RUN uv pip install --system --no-cache -r pyproject.toml

# Expose port
EXPOSE 8000

# Environment variables
ENV HOST=0.0.0.0
ENV PORT=8000
ENV DEBUG=False

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
