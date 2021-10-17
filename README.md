# Bit-coin-currency
## Description 
### Web App to output the current BitCoine price and the average price of the last 10 minutes.
## To run python app do in cmd:
```
pip install -r requirements.txt
```
Or use
```
pip3 install -r requirements.txt
```
and then do
```
py bitcoin-app.py
```
## to Build the image and run it do:
'''
docker build -t bitcoin-docker:latest .
docker run -d -p 5000:5000 bitcoin-docker
'''

### the web app sude look like this:
![Screenshot (13)](https://user-images.githubusercontent.com/91056497/137638557-e17d6f8c-23d2-447f-91e3-a605341e5904.png)

## Jenkinsfile
### Building the jenkinsfile will build the app image and push it to the DockerHub account that's specified in the Jenkinsfile
### after building jenkins file:
![Screenshot (12)](https://user-images.githubusercontent.com/91056497/137638415-64bb2e75-6bbd-4609-84f0-a103cb49cb82.png)


