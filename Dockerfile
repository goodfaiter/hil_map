# Base python image
FROM ubuntu:24.04

# Install and update system dependencies
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y --no-install-recommends python3-pip git nano mesa-utils

# Install basic python dependecies
RUN pip3 install --upgrade pip uv --break-system-packages

# Install python dependencies from pyproject.toml
WORKDIR /workspace
COPY pyproject.toml /workspace/pyproject.toml
RUN pip3 install --break-system-packages .
RUN rm -rf /workspace

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Add entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]