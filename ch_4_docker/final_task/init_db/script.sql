CREATE TABLE vehicle (
    maker VARCHAR(50),
    model VARCHAR(50) PRIMARY KEY,
    type VARCHAR(10)
);

CREATE TABLE car (
    code INT PRIMARY KEY,
    model VARCHAR(50),
    engine_power INT,
    fuel_type VARCHAR(20),
    seats INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (model) REFERENCES vehicle(model)
);

CREATE TABLE truck (
    code INT PRIMARY KEY,
    model VARCHAR(50),
    engine_power INT,
    load_capacity DECIMAL(10, 2),
    fuel_type VARCHAR(20),
    price DECIMAL(10, 2),
    FOREIGN KEY (model) REFERENCES vehicle(model)
);

CREATE TABLE motorcycle (
    code INT PRIMARY KEY,
    model VARCHAR(50),
    engine_power INT,
    fuel_type VARCHAR(20),
    weight DECIMAL(10, 2),
    price DECIMAL(10, 2),
    FOREIGN KEY (model) REFERENCES vehicle(model)
);

INSERT INTO vehicle (maker, model, type) VALUES
    ('Multi', 'MultiCar', 'Car'),
    ('Multi', 'MultiTruck', 'Truck'),
    ('Multi', 'MultiMoto', 'Motorcycle'),
    ('Duo2TC', 'Duo2Truck', 'Truck'),
    ('Duo2TC', 'Duo2Car', 'Car'),
    ('Duo4TM', 'Duo4Truck', 'Truck'),
    ('Duo4TM', 'Duo4Moto', 'Motorcycle'),
    ('Duo5CM', 'Duo5Car', 'Car'),
    ('Duo5CM', 'Duo5Moto', 'Motorcycle'),
    ('SoloC', 'SoloCar', 'Car'),
    ('SoloT', 'SoloTruck', 'Truck'),
    ('SoloM', 'SoloMoto', 'Motorcycle');

INSERT INTO truck (code, model, engine_power, load_capacity, fuel_type, price) VALUES
    (1, 'MultiTruck', 270, 1.00, 'Diesel', 1111.00),
    (2, 'Duo2Truck', 320, 2.00, 'Diesel', 2222.00),
    (3, 'Duo4Truck', 300, 4.00, 'Diesel', 3333.00),
    (4, 'SoloTruck', 310, 6.00, 'Diesel', 4444.00);

INSERT INTO car (code, model, engine_power, fuel_type, seats, price) VALUES
    (1, 'MultiCar', 180, 'Electric', 4, 1010.00),
    (2, 'Duo2Car', 350, 'Gasoline', 4, 2020.00),
    (3, 'Duo5Car', 280, 'Diesel', 6, 3030.00),
    (4, 'SoloCar', 777, 'Gasoline', 2, 4040.00);

INSERT INTO motorcycle (code, model, engine_power, fuel_type, weight, price) VALUES
    (1, 'MultiMoto', 33, 'Electric', 50.00, 101.00),
    (2, 'Duo4Moto', 33, 'Electric', 70.00, 102.00),
    (3, 'Duo5Moto', 66, 'Gasoline', 200.00, 103.00),
    (4, 'SoloMoto', 77, 'Gasoline', 210.00, 104.00);
