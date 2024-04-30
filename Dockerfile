# Use official MySQL image as base
FROM mysql:latest

# Set default environment variables
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=default_db

# Copy the SQL script to initialize the database
COPY ./db.sql /docker-entrypoint-initdb.d/

# Expose port 3306
EXPOSE 3306

# Command to run MySQL server
CMD ["mysqld"]
