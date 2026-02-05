# Base python image
FROM ubuntu:24.04

# Install and update system dependencies
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y --no-install-recommends python3-pip git nano mesa-utils

# Install basic python dependecies
RUN pip3 install --upgrade uv --break-system-packages

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Add entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]