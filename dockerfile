FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Selenium, Chrome and ChromeDriver
RUN apt-get update && \
    apt-get install -y wget gnupg unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget -O /chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip && \
    unzip /chromedriver.zip -d /usr/local/bin/ && \
    rm /chromedriver.zip

# Set display port to avoid crash
ENV DISPLAY=:99

# Adjust workdir
WORKDIR /usr/src/app

# Copy project files
COPY . /usr/src/app

# Enable script to be executed
RUN chmod +x /usr/src/app/dockerCommands.sh

# Install pytest
RUN pip3 install --upgrade pip && pip3 install pytest

# Install project dependencies
RUN pip install -r requirements.txt

# Set ChromeDriver in environment variables
ENV PATH="/usr/src/app/drivers/chromedriver-linux64:$PATH"

# Command to run the tests
CMD ["bash", "/usr/src/app/dockerCommands.sh"]