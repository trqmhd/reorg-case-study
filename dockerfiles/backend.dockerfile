# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /backend-app

# Copy the requirements file into the container
COPY ./payment-search-tool-api/requirements.txt .

# Install the dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the application files into the container
COPY ./payment-search-tool-api/. .


# Expose the port the app will run on
EXPOSE 4000

# Start the application
CMD ["python", "app.py"]
