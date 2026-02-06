CREATE OR REPLACE VIEW curated.bi_rinde_clima AS
SELECT
    r.campania,
    r.lote_id,
    r.cultivo,
    r.fecha,
    r.rinde_kg_ha,

    -- Weather aggregation (30 days before harvest)
    AVG(c.temp_max_c)           AS avg_temp_max_30d,
    AVG(c.temp_min_c)           AS avg_temp_min_30d,
    SUM(c.precipitacion_mm)     AS total_rain_30d,
    AVG(c.humedad_pct)          AS avg_humidity_30d

FROM curated.rinde_lotes r
LEFT JOIN curated.clima_diario c
ON r.lote_id = c.lote_id
AND r.campania = c.campania
AND c.fecha BETWEEN date_add('day', -30, r.fecha)
AND r.fecha

GROUP BY
    r.campania,
    r.lote_id,
    r.cultivo,
    r.fecha_cosecha,
    r.rinde_kg_ha;
