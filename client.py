# Welcome to PyShine
# This is client code to receive video and audio frames over TCP

import socket,os
import threading, wave, pyaudio, pickle,struct

def audio_stream(host_ip, port):
	p = pyaudio.PyAudio()
	CHUNK = 1024

	stream = p.open(format=p.get_format_from_width(2),
					channels=2,
					rate=44100,
					output=True,
					frames_per_buffer=CHUNK)
					
	# create socket
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket_address = (host_ip, port)
	print('server listening at',socket_address)
	client_socket.connect(socket_address) 
	print("CLIENT CONNECTED TO",socket_address)
	data = b""
	payload_size = struct.calcsize("Q")
	wf = wave.open('output.wav', 'wb')
	wf.setnchannels(2)
	wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
	wf.setframerate(44100)
	while True:
		try:
			while len(data) < payload_size:
				packet = client_socket.recv(4*1024) # 4K
				if not packet: break
				data+=packet
			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q",packed_msg_size)[0]
			while len(data) < msg_size:
				data += client_socket.recv(4*1024)
			frame_data = data[:msg_size]
			data  = data[msg_size:]
			frame = pickle.loads(frame_data)
			stream.write(frame)
            
			wf.writeframes(frame)
            
		except:

			break

	wf.close()
	client_socket.close()
	print('Audio closed')
	os._exit(1)	
    
def main():
    host_name = socket.gethostname()
    
    host_ip = input("Enter server host's ip: ")
    port = 8800
    
    t1 = threading.Thread(target=audio_stream, args=(host_ip, port))
    t1.daemon = True
    t1.start()


