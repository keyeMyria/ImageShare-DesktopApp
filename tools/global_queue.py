from queue import Queue


class GlobalQueue:
    """
    A Queue where data is put in globally, but where the data only gets removed from the private instance
    """

    def __init__(self):
        """
        Initializes the main queue and the private queue list
        """
        self.global_queue = Queue()
        self.queues = []

    def put(self, item):
        """
        Put an item into the queue and all the private queues
        :param item: Any Object that should be inserted into the queue
        :return:
        """

        self.global_queue.put(item)

        for queue in self.queues:
            queue.put(item)

    def get_new_queue(self):
        """
        Creates a new private queue which has all the data from the global queue
        :return:
        """

        queue = PrivateQueue(self)

        for item in self.to_array():
            queue.put(item)

        self.queues.append(queue)

        return queue

    def remove_queue(self, queue):
        """
        Removes a private queue from the list so it won't get any further data
        :param queue: A private queue object that is in the private queue list
        :return:
        """

        self.queues.remove(queue)

    def to_array(self):
        """
        Transforms the global queue into an array
        :return:
        """

        return list(self.global_queue.queue)

    def clear(self):
        """
        Removes all the data from the global queue and all the private queues
        :return:
        """

        self.global_queue.queue.clear()

        for queue in self.queues:
            queue.queue.clear()


class PrivateQueue(Queue):
    """
    The private queue is generated by the global queue, where it also gets all the information from
    """

    def __init__(self, global_queue):
        """
        Initializes the private queue
        :param global_queue: Object of the global Queue
        """
        Queue.__init__(self)
        self.global_queue = global_queue

    def delete_queue(self):
        """
        Removes the queue from the global queues list so it won't get any further information
        :return:
        """
        self.global_queue.remove_queue(self)
