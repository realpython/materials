import csv
import datetime
import random

random.seed(10)


def generate_pu():
    lower_bound = datetime.datetime(
        year=2021, month=1, day=1, hour=0, minute=0, second=0
    )
    upper_bound = datetime.datetime(
        year=2021, month=12, day=31, hour=23, minute=59, second=59
    )
    random_pickup = random.random() * (upper_bound - lower_bound) + lower_bound
    return random_pickup.replace(microsecond=0)


def generate_do(pick_up):
    random_dropoff = pick_up + datetime.timedelta(
        minutes=random.randint(10, 120), seconds=random.randint(0, 59)
    )
    return random_dropoff


def generate_choice(*kwargs):
    return random.choice(kwargs)


def generate_file():
    with open("2021_Yellow_Taxi_Trip_Data.csv", "w", newline="") as csvfile:
        header = (
            "VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,"
            "trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,"
            "payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,"
            "improvement_surcharge,total_amount,congestion_surcharge,airport_fee"
        ).split(",")

        writer = csv.writer(csvfile)
        writer.writerow(header)

        for _ in range(690_000_000):
            fare_amount = round(random.uniform(5.0, 100.0), 2)
            extra = generate_choice(0, 0.5, 3)
            mta_tax = generate_choice(0, 0.5)
            tip_amount = round(random.uniform(0.0, 20.0), 2)
            tolls_amount = generate_choice(0, 6.12)
            improvement_surcharge = 0.3
            congestion_surcharge = 2.5
            total_amount = round(
                fare_amount
                + extra
                + mta_tax
                + tip_amount
                + tolls_amount
                + improvement_surcharge
                + congestion_surcharge,
                2,
            )

            pick_up = generate_pu()

            ride = [
                random.randint(0, 6),  # VendorID
                pick_up,  # tpep_pickup_datetime
                generate_do(pick_up),  # tpep_dropoff_datetime
                random.randint(0, 5),  # passenger_count
                random.randint(0, 15),  # trip_distance
                random.randint(0, 6),  # RatecodeID
                generate_choice("Y", "N"),  # store_and_fwd_flag
                random.randint(1, 265),  # PULocationID
                random.randint(1, 265),  # DOLocationID
                random.randint(0, 5),  # payment_type
                fare_amount,  # fare_amount
                extra,  # extra
                mta_tax,  # mta_tax
                tip_amount,  # tip_amount
                tolls_amount,  # tolls_amount
                improvement_surcharge,  # improvement_surcharge
                total_amount,  # total_amount
                congestion_surcharge,  # congestion_surcharge
            ]

            writer.writerow(ride)


generate_file()
