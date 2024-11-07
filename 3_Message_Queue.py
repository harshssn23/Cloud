from multiprocessing import Process, Queue
import time
def sender(queue):
    message = "Hello from Sender"
    message1="hello from s2"
    queue.put(message)  # Sending message to the queue
    queue.put(message1)
    print("Sender Process: Sent message:", message)
    print("Sender Process: Sent message:", message1)
    
def receiver(queue):
    time.sleep(1)  # Wait for sender to send message
    message = queue.get()  # Receiving message from the queue
    m2=queue.get()
    print("Receiver Process: Received message:", message)
    print("Receiver Process: Received message:", m2)
if __name__ == "__main__":
    queue = Queue()

    sender_process = Process(target=sender, args=(queue,))
    receiver_process = Process(target=receiver, args=(queue,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
