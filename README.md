# Bit-coin-currency
## Description 
### Web App to output the current BitCoine price and the average price of the last 10 minutes.
## To run python app do in cmd:
'''
py bitcoin-app.py
'''
## to Build the image and run it do:
'''
docker build -t bitcoin-docker:latest .
docker run -d -p 5000:5000 bitcoin-docker
'''

### the web app sude look like this:


## Jenkinsfile
### Building the jenkinsfile will build the app image and push it to the DockerHub account that's specified in the Jenkinsfile
### after building jenkins file:
![Screenshot (12)](https://user-images.githubusercontent.com/91056497/137638415-64bb2e75-6bbd-4609-84f0-a103cb49cb82.png)


