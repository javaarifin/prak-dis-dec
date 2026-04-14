# main.py

# Impor kelas VectorClock dari modul vclocks yang telah dibuat
from vclocks import VectorClock

# Simulate a system with 3 processes 
vc0 = VectorClock(num_processes=3, process_id=0) 
vc1 = VectorClock(num_processes=3, process_id=1) 
vc2 = VectorClock(num_processes=3, process_id=2)

print("Initial States:")
print(vc0) 
print(vc1)
print(vc2)

# Process 0 performs a local event [cite: 347, 348]
print("\nEvent 1: P0 performs local event")
vc0.increment() 
print(vc0) 

# Process 0 sends a message to Process 1 [cite: 365]
print("\nEvent 2: P0 sends message to P1")
message_from_p0 = vc0.send_message() 
vc1.receive_message(message_from_p0) 
print(vc0) 
print(vc1) 

# Process 2 performs a local event [cite: 370]
print("\nEvent 3: P2 performs local event")
vc2.increment() 
print(vc2) 

# Process 1 sends a message to Process 2 [cite: 373]
print("\nEvent 4: P1 sends message to P2")
message_from_p1 = vc1.send_message() 
vc2.receive_message(message_from_p1) 
print(vc1) 
print(vc2) 

# Check causality [cite: 380]
print("\nCausality Checks:")
print(f"vc0 happens before vc1: {vc0.happens_before(vc1)}") 
print(f"vc1 happens before vc0: {vc1.happens_before(vc0)}") 
print(f"vc0 is concurrent with vc2: {vc0.is_concurrent(vc2)}") 