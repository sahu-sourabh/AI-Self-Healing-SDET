# 1. Use an official lightweight Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (to leverage Docker caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Set the PYTHONPATH so Python can find your 'app' folder
ENV PYTHONPATH=/app

# 7. The command to run your tests when the container starts
CMD ["pytest", "tests/test_unified_flow.py", "-v"]