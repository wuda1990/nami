from kafka import KafkaProducer


def create_producer():
    producer = KafkaProducer(
        bootstrap_servers=['10.181.60.94:9094'],  # 使用OUTSIDE监听器的端口和地址
        value_serializer=lambda x: x.encode('utf-8')  # 消息内容编码为utf-8
    )
    return producer


def send_message(producer, topic, message):
    try:
        # 发送消息
        future = producer.send(topic, value=message)
        result = future.get(timeout=3)  # 等待消息发送完成
        print('Message sent:', result)
    except Exception as e:
        print('Failed to send message:', str(e))


def main():
    producer = create_producer()
    topic = 'input'  # 假设使用了配置中的一个topic
    message = 'Hello, Kafka!'
    send_message(producer, topic, message)
    producer.close()


if __name__ == '__main__':
    main()
