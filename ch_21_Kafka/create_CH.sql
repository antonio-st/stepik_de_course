CREATE TABLE raw_fish (
  species String,
  length String,
  weight String,
  w_l_ratio String
) ENGINE = Kafka
SETTINGS 
  kafka_broker_list = '192.168.100.11:9092', -- поменять на свой
  kafka_topic_list = 'fish',
  kafka_group_name = 'clickhouse_reader', 
  kafka_format = 'JSONEachRow';


CREATE TABLE fish_data (
  fish_name String,
  fish_length Float32,
  fish_weight Float32,
  w_l_ratio Float32 
) ENGINE = MergeTree()
ORDER BY (fish_name);

CREATE MATERIALIZED VIEW fish_processing TO fish_data AS
    SELECT
        species as fish_name,
        length as fish_length,
        weight as fish_weight,
        w_l_ratio as w_l_ratio
    FROM raw_fish; 
