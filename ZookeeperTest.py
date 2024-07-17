from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.protocol.states import WatchedEvent


class ZooKeeperClient:
    def __init__(self, hosts='127.0.0.1:2181'):
        self.zk = KazooClient(hosts=hosts)
        self.zk.add_listener(self.my_listener)
        self.zk.start()

    def my_listener(self, state):
        if state == KazooState.LOST:
            print("Lost connection to ZooKeeper")
        elif state == KazooState.SUSPENDED:
            print("Connection suspended")
        else:
            print("Connected to ZooKeeper")

    def watch_node(self, event):
        if event.type == "CHANGED":
            data, stat = self.zk.get(event.path)
            print("Node data changed to:", data.decode("utf-8"))

    def setup_watch(self, path):
        self.zk.get(path, watch=self.watch_node)
        self.zk.set(path, "new data".encode("utf-8"))

    def create_node(self, path, data):
        if not self.zk.exists(path):
            self.zk.create(path, data.encode("utf-8"), makepath=True)
        self.setup_watch(path)

    def close(self):
        self.zk.stop()


if __name__ == '__main__':
    zk_client = ZooKeeperClient()
    try:
        path = "/my/favorite/node"
        zk_client.create_node(path, "hello world")
        import time

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping ZooKeeper client")
    finally:
        zk_client.close()
