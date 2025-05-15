def ha_publish_position(client, base_topic, rcv):
    client.publish(topic=base_topic + "/" + rcv["blind_id"] + "/status",
               payload=rcv["position"])


class HomeAssistant:
    pass