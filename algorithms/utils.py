# import pandas as pd
# import random

# # this function will geenrate our randomg trips to use as data
# def generate_sample_trips(num_trips):
#     trips = []
#     for _ in range(num_trips):
#         u = random.randint(1, 10)  # Start station vertex
#         v = random.randint(1, 10)  # End station vertex
#         while u == v:  #start and end should not be same
#             v = random.randint(1, 10)
#         dep = random.randint(0, 10)  # Departure time in minutes
#         dur = random.randint(1, 5)  # Duration of the trip in minutes
#         vid = random.randint(1, 3)  # vehicle iD 1, 2, or 3
#         trips.append((u, v, dep, dur, vid))
#     return trips

# #  to save generated trips to a CSV file
# def save_to_csv(trips, filename):
#     df = pd.DataFrame(trips, columns=["u", "v", "dep", "dur", "vid"])
#     df.to_csv(filename, index=False)
#     print(f"Data saved to {filename}")

# #  to load trips from a CSV file
# def load_from_csv(filename):
#     df = pd.read_csv(filename)
#     return df.values.tolist()
import random
import csv

def generate_sample_trips(num_trips, num_stations=10, num_vehicles=3):
    # 1) Give each station a fixed vehicle ID once
    station_vid = {
        s: random.randint(1, num_vehicles)
        for s in range(1, num_stations+1)
    }

    trips = []
    # THIS LOOP IS ESSENTIAL — it creates your num_trips entries
    for _ in range(num_trips):
        u = random.randint(1, num_stations)
        v = random.randint(1, num_stations)
        while v == u:                  # ensure u != v
            v = random.randint(1, num_stations)

        dep = random.randint(0, 60)    # departure time
        dur = random.randint(1, 10)    # duration
        vid = station_vid[u]           # reuse station u’s vehicle ID

        trips.append((u, v, dep, dur, vid))
    return trips


def save_to_csv(trips, path):
    with open(path, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['u','v','dep','dur','vid'])
        writer.writerows(trips)


def load_from_csv(path):
    with open(path, newline='') as fin:
        reader = csv.DictReader(fin)
        return [
            (int(r['u']), int(r['v']),
             int(r['dep']), int(r['dur']),
             int(r['vid']))
            for r in reader
        ]
