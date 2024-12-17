# Use a lightweight Python image for the base
FROM python:3.9-slim

# Set the working directory for the container
WORKDIR /app

# Copy the project directory from the host
COPY . .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose the port where Django will run (default 8000)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#assume some kind of chnage in the code.
#comment
