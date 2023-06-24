import rclpy
from rclpy.node import Node

from std_msgs.msg import String #TODO импортировать нужный тип топика

from robonomicsinterface import  Account, Datalog

from config import (
    SEED,
)


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String, #TODO заменить тип сообщения
            'topic', #TODO заменить путь топика
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.account = Account(seed=SEED)
        self.datalog = Datalog(self.account)

    def listener_callback(self, msg):
        data = msg #TODO обработка сообщения
        if (0 < 1): #TODO придумать условие
            self.datalog.record('{"status": "success"}')
        else:
            self.datalog.record('{"status": "error"}')





def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    rclpy.shutdown()


if __name__ == '__main__':
    main()