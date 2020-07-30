# Python FIFO Queue

The queue implemented in implementation/queue.py comprises a doubly linked node structure, which uses links between nodes to point to previous and next nodes. Following the first in first out (FIFO) principle, nodes are added to the tail and removed from the head. 

A bytearray was used to store all excess node values (values that were added when the max_in_memory variable limit was exceeded) in RAM. The length of the appended bytearray() was used to determine the number of items in RAM memory. Furthermore, excess nodes were saved to disk via pickle.dump to a .obj file. As the number of nodes that were saved to disk equal the number of values appended to the bytearray, the length of the bytearray was also used to determine the number of nodes saved to disk.

Unit tests, in implementation_tests/test_queue.py, comprise tests of the essential functions to accurately infer correctness of other functions. Test_in_memory_count() success affirms that both in_memory_count() and on_disk_count() are correct. Enqueue() is used in all tests, thus it may be concluded that this function is correct.

External sources used for tips and inspiration:
1. persist-queue @ GitHub: https://github.com/peter-wangxu/persist-queue/blob/master/persistqueue/queue.py
2. cpython queue.py @ GitHub: https://github.com/python/cpython/blob/3.8/Lib/queue.py
3. Python 3.8 Documentation: https://docs.python.org/3.8/index.html

It took 4 hours to complete this project.
