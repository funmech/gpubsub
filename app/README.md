export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/gcp_keys/foodtrustplatform-pubsub.json

source ../envs/bin/activate
python quickstart.py foodtrustplatform scanevent-geocodes geocodes-parser
