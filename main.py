from algorithms import sq_min_transfers, nq_min_transfers, mq_min_transfers
from algorithms.tpp_graph import TPPGraph
from algorithms.utils import generate_sample_trips, save_to_csv, load_from_csv
import time


def time_algo(name, fn, tpp, source):
    start = time.perf_counter()
    result = fn(tpp, source)
    elapsed = (time.perf_counter() - start) * 1000  # ms
    print(f"{name} took {elapsed:.2f}ms → {result}")
    
    
def run():
    # i ran this commented out code for first time to geenrate data,then commented it out since i got data so no need to run again
    # small_sample = generate_sample_trips(5)
    # medium_sample = generate_sample_trips(50)
    # large_sample = generate_sample_trips(500)
    
    

    # # save_to_csv(small_sample, 'data/small_sample.csv')
    # save_to_csv(medium_sample, 'data/medium_sample.csv')
    # save_to_csv(large_sample, 'data/large_sample.csv')

    # Load the datasets for testing
    small_trips = load_from_csv('data/small_sample.csv')
    medium_trips = load_from_csv('data/medium_sample.csv')
    large_trips = load_from_csv('data/large_sample.csv')
    
    print(" for small Sample Trips:", small_trips) 
    print("reached till here hehehe") 


    
    tpp_small = TPPGraph(small_trips)
    tpp_medium=TPPGraph(medium_trips)
    tpp_large=TPPGraph(large_trips)
    
    for src in [1, 2,4]:
        
        print(f"\n===== Source = {src} on Small Sample =====")
        tpp = tpp_small  # your 5‑trip graph
        time_algo("SQ", sq_min_transfers, tpp, src)
        time_algo("NQ", nq_min_transfers, tpp, src)
        time_algo("MQ", mq_min_transfers, tpp, src)
        
        print(f"\n===== Source = {src} on Medium Sample =====")
        tpp = tpp_medium  # your 50‑trip graph
        time_algo("SQ", sq_min_transfers, tpp, src)
        time_algo("NQ", nq_min_transfers, tpp, src)
        time_algo("MQ", mq_min_transfers, tpp, src)

        print(f"\n===== Source = {src} on Large Sample =====")
        tpp = tpp_large  # your 500‑trip graph
        time_algo("SQ", sq_min_transfers, tpp, src)
        time_algo("NQ", nq_min_transfers, tpp, src)
        time_algo("MQ", mq_min_transfers, tpp, src)
    

    
    # source = 1  # Assuming station 1 is the source
    # print("SQ:", sq_min_transfers(tpp_small, source))
    # print("NQ:", nq_min_transfers(tpp_small, source))
    # print("MQ:", mq_min_transfers(tpp_small, source))
    # print("PQ:", pq_min_transfers(tpp_small, source))
    # print("MPQ:", mpq_min_transfers(tpp_small, source))

if __name__ == "__main__":
    run()
