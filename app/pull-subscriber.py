import argparse
import time

from google.cloud import pubsub_v1


def pull(project_id, subscription_name):
    # [START pubsub_end_to_end]

    # Instantiates a subscriber client
    subscriber = pubsub_v1.SubscriberClient()

    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    switch = []
    def callback(message):
        print('Received message: {}'.format(message))
        # Unacknowledged messages will be sent again.
        message.ack()
        print(message.data.decode('utf-8'))
        switch.append(True)

    subscribe_begin = time.time()

    # Receive messages. The subscriber is nonblocking.
    subscriber.subscribe(subscription_path, callback=callback)

    print('\nListening for messages on {}...\n'.format(subscription_path))
    count = 0
    while True:
        if count > 500:
            subscribe_time = time.time() - subscribe_begin
            print("\nReceived all messages.")
            print("Subscribe time lapsed: {:.2f}s.".format(subscribe_time))
            print("Total messages received %d" % len(switch))
            break
        else:
            # Sleeps the thread at 50Hz to save on resources.
            count += 1
            time.sleep(1. / 50)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('project_id', help='Your Google Cloud project ID')
    parser.add_argument('subscription_name', help='Your subscription name')

    args = parser.parse_args()

    pull(args.project_id, args.subscription_name)
