from algorithms import sq_min_transfers, nq_min_transfers, mq_min_transfers, pq_min_transfers, mpq_min_transfers
from algorithms.tpp_graph import TPPGraph
from algorithms.utils import generate_sample_trips, save_to_csv, load_from_csv

def run():
    # Generate and save sample datasets
    small_sample = generate_sample_trips(5)
    medium_sample = generate_sample_trips(50)
    large_sample = generate_sample_trips(500)
    
    

    save_to_csv(small_sample, 'data/small_sample.csv')
    save_to_csv(medium_sample, 'data/medium_sample.csv')
    save_to_csv(large_sample, 'data/large_sample.csv')

    # Load the datasets for testing
    small_trips = load_from_csv('data/small_sample.csv')
    medium_trips = load_from_csv('data/medium_sample.csv')
    large_trips = load_from_csv('data/large_sample.csv')
    
    print(" for small Sample Trips:", small_trips)  


    
    tpp_small = TPPGraph(small_trips)

    # Test the algorithms on the small dataset
    source = 1  # Assuming station 1 is the source
    print("SQ:", sq_min_transfers(tpp_small, source))
    print("NQ:", nq_min_transfers(tpp_small, source))
    print("MQ:", mq_min_transfers(tpp_small, source))
    print("PQ:", pq_min_transfers(tpp_small, source))
    print("MPQ:", mpq_min_transfers(tpp_small, source))

if __name__ == "__main__":
    run()
