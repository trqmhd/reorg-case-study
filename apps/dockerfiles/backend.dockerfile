# Use the official Python base image
FROM python:3.9

# # Add main repository
# RUN echo "deb http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list

# # Update repositories and install packages
# RUN apt-get update
# RUN apt-get install -y --allow-downgrades libssl-dev
# RUN apt-get install -y default-libmysqlclient-dev build-essential


# RUN apt-get update && \
#     apt-get install -y gnupg && \
#     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8C718D3B5072E1F5 && \
#     echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-5.7" > /etc/apt/sources.list.d/mysql.list && \
#     apt-get update && \
#     apt-get install -y mysql-client libmariadbclient-dev && \
#     apt-get remove -y gnupg && \
#     apt-get autoremove -y && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



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
