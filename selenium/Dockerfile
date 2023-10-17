FROM selenium/standalone-chrome:latest

USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Create downloads directory
RUN mkdir /home/seluser/downloads 

# Install Python packages
RUN pip3 install selenium bs4 lxml docker

# Remove the existing chromedriver symbolic link
RUN rm /usr/bin/chromedriver

# Copy the downloaded ChromeDriver
COPY ./path/to/chromedriver /usr/bin/chromedriver

# Set permissions
RUN chown seluser:seluser /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

# Switch back to the seluser user
USER seluser

# Copy the Python script
COPY ../external/webscrapping/get_data.py /home/seluser/

# Set the working directory
WORKDIR /home/seluser/
