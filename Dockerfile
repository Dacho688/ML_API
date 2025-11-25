# Dockerfile
# Use a lightweight official Python image as the base
FROM python:3.12-slim
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of your application code
COPY ./app .
# Expose the port your FastAPI application will run on
EXPOSE 7860
# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]