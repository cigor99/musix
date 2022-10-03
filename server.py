import socket
import threading, wave, pyaudio,pickle,struct

def audio_stream(host_ip, port, input_device):
    server_socket = socket.socket()
    server_socket.bind((host_ip, port))

    server_socket.listen(5)
    CHUNK = 1024
    
    p = pyaudio.PyAudio()
    print('server listening at',(host_ip, port))
   
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=44100,
                    input=True,
                    input_device_index = input_device,
                    frames_per_buffer=CHUNK)

             

    client_socket,addr = server_socket.accept()
 
    data = None
    while True:
        if client_socket:
            while True:
              
                data = stream.read(CHUNK)
                a = pickle.dumps(data)
                message = struct.pack("Q",len(a))+a
                client_socket.sendall(message)
                
def start_stream():
    host_name = socket.gethostname()
    
    print("To see your IP enter ipconfig in terminal\nIt will be ipv4 addres under Ethernet adapter Ethernet:")
    host_ip = input("input host ip: ")
    
    port = 8800
    
    input_device = int(input("Input device index: "))
    
    t1 = threading.Thread(target=audio_stream, args=(host_ip, port, input_device))
    t1.daemon = True
    t1.start()
    
def print_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))
        print()

def main():
    while True:
        print("1 Print devices")
        print("2 Start Streaming")
        print("x Exit")
        
        what_to_do = input(">> ")
        
        if what_to_do.lower() == "1":
            print_devices()
        elif what_to_do.lower() == "2":
            start_stream()
        elif what_to_do.lower() == "x":
            break

if __name__ == "__main__":
    main()