from multiprocessing import Process, shared_memory
import numpy as np
ARRAY_SIZE = 10

def writer(shared_name):
    shm = shared_memory.SharedMemory(name=shared_name) #............................................
    shared_array = np.ndarray((ARRAY_SIZE,), dtype=np.int32, buffer=shm.buf)  #.....................
    for i in range(ARRAY_SIZE):
        shared_array[i] = i * 10  # Example: writing multiples of 10  
    print("Writer: Data written to shared memory.")
    shm.close()

def reader(shared_name):
    shm = shared_memory.SharedMemory(name=shared_name) #...........................................
    shared_array = np.ndarray((ARRAY_SIZE,), dtype=np.int32, buffer=shm.buf)  #....................
    print("Reader: Data read from shared memory:", shared_array[:])
    shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=ARRAY_SIZE * np.int32().nbytes) #...........
    writer_process = Process(target=writer, args=(shm.name,))
    writer_process.start()
    writer_process.join()
    
    reader_process = Process(target=reader, args=(shm.name,))
    reader_process.start()
    reader_process.join()
    # shm.close()
    # shm.unlink()
