import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# send message to get answer
socket.send_string("what is in the dict")

reply = socket.recv_string()
print("Server answer:", reply)
