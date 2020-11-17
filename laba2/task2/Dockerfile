
# using httpd image
FROM httpd

# copy current directory with brat to container
COPY . .

# update packages
RUN apt-get update && apt-get install -y python

# Create args for the shell-script
ARG user_name
ARG password
ARG admin_email

# installation script
RUN sh install.sh $user_name $password $admin_email

# Port
EXPOSE 8001

# Start the server
CMD ["python", "standalone.py"]