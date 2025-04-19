import pandas as pd
import random

# this function will geenrate our randomg trips to use as data
def generate_sample_trips(num_trips):
    trips = []
    for _ in range(num_trips):
        u = random.randint(1, 10)  # Start station vertex
        v = random.randint(1, 10)  # End station vertex
        while u == v:  #start and end should not be same
            v = random.randint(1, 10)
        dep = random.randint(0, 10)  # Departure time in minutes
        dur = random.randint(1, 5)  # Duration of the trip in minutes
        vid = random.randint(1, 3)  # vehicle iD 1, 2, or 3
        trips.append((u, v, dep, dur, vid))
    return trips

#  to save generated trips to a CSV file
def save_to_csv(trips, filename):
    df = pd.DataFrame(trips, columns=["u", "v", "dep", "dur", "vid"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

#  to load trips from a CSV file
def load_from_csv(filename):
    df = pd.read_csv(filename)
    return df.values.tolist()
