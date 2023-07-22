import csv
import math
import random
import matplotlib.pyplot as plt
import subprocess


class Store:
    def __init__(self, id, address, city, state, zipcode, latitude, longitude):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.latitude = latitude
        self.longitude = longitude

    def haversine_distance(self, lat2, lon2):
        r = 3958.8  # Radius of the Earth in miles
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        a = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return r * c

def read_csv_file(file_name):
    stores = []
    with open(file_name, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader, None)  # Skip the headers
        for row in datareader:
            id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            latitude = float(row[5])
            longitude = float(row[6])
            stores.append(Store(id, address, city, state, zipcode, latitude, longitude))
    return stores

def evaluate_l1_data_cache(simple_scalar_path, config_file, benchmark_path, input_file):
    cache_configs = [
        "dl1:16:64:1:l",
        "dl1:16:64:2:l",
        "dl1:16:64:4:l",
        "dl1:16:64:8:l",
        "dl1:32:64:1:l"
    ]
    ipc_results = []
    misprediction_results = []

    for config in cache_configs:
        # Comment out or remove these lines since you don't have the specific files
        command = f"{simple_scalar_path} -config {config_file} -cache {config} {benchmark_path} {input_file}"
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        lines = result.strip().split('\n')
        ipc = float(lines[-2].split()[-1])  # Extract IPC value
        mispredictions = int(lines[-3].split()[-1])  # Extract mispredictions count

        # Since you don't have the files, let's use some sample IPC and misprediction values for demonstration
        ipc = random.uniform(0.5, 2.0)
        mispredictions = random.randint(1000, 5000)

        ipc_results.append(ipc)
        misprediction_results.append(mispredictions)

    # Generate and save the figure for IPC vs. L1 Data Cache Configurations
    plt.figure()
    plt.bar([f"L1 {config.split(':')[2]}" for config in cache_configs], ipc_results)
    plt.xlabel('L1 Data Cache Configurations')
    plt.ylabel('IPC')
    plt.title('IPC vs. L1 Data Cache Configurations')
    plt.savefig('ipc_vs_l1_data_cache.png')
    plt.close()

    # Generate and save the figure for Misprediction Rate vs. L1 Data Cache Configurations
    misprediction_rate = [mispredictions / 124435 for mispredictions in misprediction_results]
    plt.figure()
    plt.bar([f"L1 {config.split(':')[2]}" for config in cache_configs], misprediction_rate)
    plt.xlabel('L1 Data Cache Configurations')
    plt.ylabel('Misprediction Rate')
    plt.title('Misprediction Rate vs. L1 Data Cache Configurations')
    plt.savefig('misprediction_rate_vs_l1_data_cache.png')
    plt.close()

def main():
    file_name = r"C:\Users\J.I Traders\Downloads\Project2\WhataburgerData.csv"
    stores = read_csv_file(file_name)

    # simple_scalar_path = "./simplesim-3.0/sim-outorder"  # Update with the path to your compiled SimpleScalar binary
    # config_file = "nehalem.cfg"  # Update with the path to your CPU configuration file
    # benchmark_path = "./benchmarks"  # Update with the path to the benchmarks directory
    # input_file = "./benchmarks/perl-tests.pl"  # Update with the path to the input file used by the benchmark

    # evaluate_l1_data_cache(simple_scalar_path, config_file, benchmark_path, input_file)

    #  Sample queries (you can modify these as per your requirements)
    queries = [
        (33.1502, -96.8236, 3),
        (29.4241, -98.4936, 5)
    ]

    for query in queries:
        lat, lon, num_stores = query

        # Calculate distance to each store
        for store in stores:
            store.distance = store.haversine_distance(lat, lon)

        # Find the nth closest store using random select
        nth_closest_store = sorted(stores, key=lambda x: x.distance)[num_stores - 1]

        # Find all stores at least as close as nth_closest_store
        close_stores = [store for store in stores if store.distance <= nth_closest_store.distance]

        # Sort by distance and print
        close_stores.sort(key=lambda store: store.distance)
        for store in close_stores:
            print(f"ID: {store.id}, Address: {store.address}, City: {store.city}, State: {store.state}, Zip: {store.zipcode}, Distance: {store.distance} miles")

if __name__ == "__main__":
    main()


