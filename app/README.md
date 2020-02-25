```shell
export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/gcp_keys/foodtrustplatform-pubsub.json

source ../envs/bin/activate
# create scanevent-geocodes if not yet
# gcloud pubsub topics create scanevent-geocodes
# publish 1 message
python publisher.py foodtrustplatform scanevent-geocodes
# should pull all of them form geocodes-parser-subscription
# geocodes-parser-subscription has to be created before pulling
# gcloud pubsub subscriptions create geocodes-parser-subscription --topic myTopic
python pull-subscriber.py foodtrustplatform geocodes-parser-subscription
```