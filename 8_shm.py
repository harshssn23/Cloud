from multiprocessing import Process,shared_memory
# import time
import numpy as np
ARRAY_SIZE=10

def sender(shared_name):
    shm=shared_memory.SharedMemory(name=shared_name) #..................
    # shared_array=((ARRAY_SIZE,),buffer=shm.buf)
    shared_array=np.ndarray((ARRAY_SIZE),dtype=np.int32,buffer=shm.buf) #..............................
    for i in range(10):
        shared_array[i]=i*10
    print("Writer wrote 10's table in shared memory")
    shm.close()

def receiver(shared_name):
    shm=shared_memory.SharedMemory(name=shared_name)
    shared_array=np.ndarray((ARRAY_SIZE),dtype=np.int32,buffer=shm.buf)
    print("Receiver reads data in shared memory:", shared_array[:])
    shm.close()

if __name__=='__main__':
    shm=shared_memory.SharedMemory(create=True,size=(ARRAY_SIZE)) #.......................
    sender_process=Process(target=sender,args=(shm.name,))
    sender_process.start()
    sender_process.join()
    receiver_process=Process(target=receiver,args=(shm.name,))
    receiver_process.start()
    receiver_process.join()



