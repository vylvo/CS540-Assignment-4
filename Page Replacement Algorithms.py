
from collections import deque, OrderedDict

def fifo(pages, frames_count):
    frame = deque()
    faults = 0
    fault_steps = []

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frames_count:
                frame.append(page)
            else:
                frame.popleft()
                frame.append(page)
            faults += 1
            fault_steps.append(f"Step {i+1}: Page fault ({page}) - Frames: {list(frame)}, Faults: {faults}")
    
    return fault_steps, faults

def lru(pages, frames_count):
    frame = OrderedDict()
    faults = 0
    fault_steps = []

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) >= frames_count:
                frame.popitem(last=False)
            frame[page] = i
            faults += 1
            fault_steps.append(f"Step {i+1}: Page fault ({page}) - Frames: {list(frame.keys())}, Faults: {faults}")
        else:
            frame.move_to_end(page)
    
    return fault_steps, faults

def optimal(pages, frames_count):
    frame = []
    faults = 0
    fault_steps = []

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frames_count:
                frame.append(page)
            else:
                future_uses = {f: (pages[i:].index(f) if f in pages[i:] else float('inf')) for f in frame}
                evict_page = max(future_uses, key=future_uses.get)
                frame.remove(evict_page)
                frame.append(page)
            faults += 1
            fault_steps.append(f"Step {i+1}: Page fault ({page}) - Frames: {frame}, Faults: {faults}")
    
    return fault_steps, faults

# Sample input
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames_count = 4

# Check input validity
if not all(isinstance(p, int) for p in pages) or not isinstance(frames_count, int) or frames_count <= 0:
    raise ValueError("Pages must be integers and frames_count must be a positive integer.")

# Run the simulations
fifo_output, fifo_faults = fifo(pages, frames_count)
lru_output, lru_faults = lru(pages, frames_count)
optimal_output, optimal_faults = optimal(pages, frames_count)

# Print outputs
print("For FIFO Algorithm:")
for step in fifo_output:
    print(f"• {step}")
print(f"• Total Page Faults: {fifo_faults}")

print("\nFor LRU Algorithm:")
for step in lru_output:
    print(f"• {step}")
print(f"• Total Page Faults: {lru_faults}")

print("\nFor Optimal Algorithm:")
for step in optimal_output:
    print(f"• {step}")
print(f"• Total Page Faults: {optimal_faults}")