#!/bin/bash

# Go to tmp directory
cd /tmp

# Verify if test.txt file exists, delete if exists
if test -f test.txt; then
    echo "File exists! Procceding to delete..."
    rm test.txt
else
    echo "File don't exist."
fi

# Create test.txt file
touch test.txt

# Write in file
echo "Adding content to file" >> test.txt

# Print file
cat test.txt

# Pytest asserting
python -c "print(1 + 1)"
pytest -s /usr/src/app/soma.py

# Selenium/Pytest run
pytest -s /usr/src/app/e2e_tests/tap_full.py

# Remove comment to keep container executing
# tail -f /dev/null

exec "$@"