CREATE TABLE IF NOT EXISTS cpu_temperature(
    id SERIAL PRIMARY KEY,
    temperature FLOAT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE MATERIALIZED VIEW IF NOT EXISTS cpu_temperature_aggregated AS
    SELECT 
        DATE_TRUNC('hour', recorded_at) AS hour,
        AVG(temperature) AS avg_temperature,
        MIN(temperature) AS min_temperature,
        MAX(temperature) AS max_temperature
    FROM cpu_temperature
    GROUP BY hour;