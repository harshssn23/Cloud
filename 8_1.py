from multiprocessing import Process, shared_memory
import numpy as np
# Define the size of the shared array
ARRAY_SIZE = 10
def writer(shared_name):
    # Attach to the shared memory segment created by the main process
    shm = shared_memory.SharedMemory(name=shared_name)
    # Create a NumPy array backed by the shared memory
    shared_array = np.ndarray((ARRAY_SIZE,), dtype=np.int32, buffer=shm.buf)
    
    # Write some data into the shared memory array
    for i in range(ARRAY_SIZE):
        shared_array[i] = i * 10  # Example: writing multiples of 10  
    print("Writer: Data written to shared memory.")
    shm.close()
def reader(shared_name):
    # Attach to the shared memory segment created by the main process
    shm = shared_memory.SharedMemory(name=shared_name)
    # Create a NumPy array backed by the shared memory
    shared_array = np.ndarray((ARRAY_SIZE,), dtype=np.int32, buffer=shm.buf)   
    # Read the data from the shared memory array
    print("Reader: Data read from shared memory:", shared_array[:])
    shm.close()
if __name__ == "__main__":
    # Create a shared memory segment
    shm = shared_memory.SharedMemory(create=True, size=ARRAY_SIZE * np.int32().nbytes)
    # Start the writer process
    writer_process = Process(target=writer, args=(shm.name,))
    writer_process.start()
    writer_process.join()
    
    # Start the reader process
    reader_process = Process(target=reader, args=(shm.name,))
    reader_process.start()
    reader_process.join()
    
    # Clean up shared memory
    shm.close()
    shm.unlink()
