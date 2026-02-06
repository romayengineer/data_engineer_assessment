import os
import csv
import random
from datetime import datetime, timedelta


# Random helper data
campañas = ["2023/24", "2024/25", "2025/26"]

# Generate random rows
num_rows = 10_000
start_date = datetime(2024, 1, 1)


def generate_clima_diario(num_rows):
    # Output file
    filename = "data/clima_diario.csv"

    # Column headers
    columns = ["lote_id", "campaña", "fecha", "temp_min_c", "temp_max_c", "precipitacion_mm"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)

        for i in range(1, num_rows + 1):
            lote_id = f"L{i:06d}"
            campaña = random.choice(campañas)
            fecha = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")

            temp_min = round(random.uniform(5, 20), 1)
            temp_max = round(random.uniform(temp_min + 5, temp_min + 15), 1)

            precipitacion = round(random.uniform(0, 50), 1)

            writer.writerow([lote_id, campaña, fecha, temp_min, temp_max, precipitacion])

    print(f"new CSV: {filename}")


def generate_rinde_lotes(num_rows):
    # Output file
    filename = "data/rinde_lotes.csv"

    cultivos = ["Soja", "Maiz", "Trigo"]

    # Column headers
    columns = ["lote_id", "campaña", "fecha", "cultivo", "superficie_ha", "rinde_kg_ha", "humedad_pct"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)

        for i in range(1, num_rows + 1):
            lote_id = f"L{i:06d}"
            campaña = random.choice(campañas)
            fecha = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")

            cultivo = random.choice(cultivos)

            superficie_ha = round(random.uniform(20, 70), 1)

            rinde_kg_ha = round(random.uniform(3000, 10000), 1)

            humedad_pct = round(random.uniform(10, 15), 2)

            writer.writerow([lote_id, campaña, fecha, cultivo, superficie_ha, rinde_kg_ha, humedad_pct])

    print(f"new CSV: {filename}")


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    generate_clima_diario(num_rows)
    generate_rinde_lotes(num_rows)
