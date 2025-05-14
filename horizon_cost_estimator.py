import openstack

def calculate_volume_cost():
    # Connessione al cloud
    conn = openstack.connect()

    # Recupero dei volumi
    volumes = conn.block_storage.volumes()

    total_size_gb = 0
    num_volumes = 0

    # Somma delle dimensioni e conteggio dei volumi
    for vol in volumes:
        total_size_gb += vol.size
        num_volumes += 1

    # Costi fittizi (puoi modificarli)
    cost_per_gb = 0.05       # €0,05 per GB
    cost_per_volume = 2.0    # €2,00 per volume

    total_cost = (total_size_gb * cost_per_gb) + (num_volumes * cost_per_volume)

    return {
        "total_size_gb": total_size_gb,
        "num_volumes": num_volumes,
        "estimated_cost": total_cost
    }

if __name__ == "__main__":
    result = calculate_volume_cost()
    print(f"Total Size (GB): {result['total_size_gb']}")
    print(f"Number of Volumes: {result['num_volumes']}")
    print(f"Estimated Cost: €{result['estimated_cost']:.2f}")
