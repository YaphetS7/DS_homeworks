# Dockerize brat (https://brat.nlplab.org/index.html)

---

### For build run the command:

* docker build --build-arg user_name=<daniil> --build-arg password=<password> --build-arg admin_email=<email> -t brat .
  
  
### For start run the command:

#### Foreground:

* docker run -p 8001:8001 brat


#### Background:

* docker run -d -p 8001:8001 brat


### Changing ports:

If u want to change port, u should to:
1) Change EXPOSE line in Dockerfile 
2) Change ports in starting command
3) Change the _DEFAULT_SERVER_PORT param 
