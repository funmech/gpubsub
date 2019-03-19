export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/ftp-bo-dev-pubsub.json

source ../envs/bin/acativate
python quickstart.py foodtrustplatform scanevent-geocodes geocodes-parser 2
