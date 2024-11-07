from multiprocessing import Process, Value
import time

def writer(shared_data):
    shared_data.value = 42  # Writing data into shared memory
    print("Writer Process: Written data:", shared_data.value)

def reader(shared_data):
    time.sleep(1)  # Wait for writer to write data
    print("Reader Process: Read data:", shared_data.value)

if __name__ == "__main__":
    shared_data = Value('i', 0)  # Initialize shared memory (integer)

    writer_process = Process(target=writer, args=(shared_data,))
    reader_process = Process(target=reader, args=(shared_data,))

    writer_process.start()
    reader_process.start()

    writer_process.join()
    reader_process.join()
