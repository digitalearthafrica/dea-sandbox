#!/bin/bash --login
set -e

# Update deafrica-tools
pip install deafrica-tools --upgrade --quiet

exec "$@"