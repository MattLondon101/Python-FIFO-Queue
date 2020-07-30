from take_home.implementation.queue import Queue

def test_peek():
    ''' Simple test of the peek method. '''
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.peek() == 1

def test_count():
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.count == 1

def test_dequeue():
    queue = Queue(10)
    queue.enqueue(1)
    queue.dequeue()
    assert queue.count == 1

def test_in_memory_count():
    queue = Queue(10)
    queue.enqueue(1)
    queue.enqueue(1)
    assert queue.in_memory_count == 2


