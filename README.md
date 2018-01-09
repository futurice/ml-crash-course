# ml-crash-course


## Steps to update notebook in Jupyterhub for all users

1. Get aws.pem file from brent
1. Do the following
    ```bash
    ssh -i <aws.pem> ec2-18-194-145-109.eu-central-1.compute.amazonaws.com:8000
    cd ml-crash-course
    git pull
    sudo -i
    cd /home/ec2-user/ml-crash-course
    ./copy_file.py <notebook_name> <number_of_users>
    ```

### Log in to jupyterhub
1. You must be on either **Futurice-Helsinki** or **Futurice-Guest-Helsinki** WiFi. 
1. Go to *http://ec2-18-194-145-109.eu-central-1.compute.amazonaws.com:8000* or *http://18.194.145.109:8000/*
1. There are 20 users all with the same password. 
    * username: user1, user2, user3, etc. 
    * password: jupyter*


