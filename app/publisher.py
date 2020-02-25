import argparse
import time

from google.cloud import pubsub_v1


def publish(project_id, topic_name):
    """Publish some messages"""

    # Instantiates a publisher and subscriber client
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()

    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = subscriber.topic_path(project_id, topic_name)

    publish_begin = time.time()

    # Publish messages.
    # Data must be a bytestring
    data = "-41.3296986219587,146.685017595253".encode('utf-8')

    count = 0
    while True:
        if count > 0:
            print("Total messages published %d" % count)
            break
        else:
            # Publish a message then sleeps 0.5s
            count += 1
            # When you publish a message, the client returns a future.
            future = publisher.publish(topic_path, data=data)
            print("Message count %d" % count)
            print('Published {} of message ID {}.'.format(data, future.result()))

            time.sleep(0.5)

    publish_time = time.time() - publish_begin

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('project_id', help='Your Google Cloud project ID')
    parser.add_argument('topic_name', help='Your topic name')

    args = parser.parse_args()

    publish(args.project_id, args.topic_name)
