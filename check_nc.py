from pathlib import Path
import xarray as xr
import matplotlib.pyplot as plt

path = Path(r"D:\projects\Flood_Model\earth_sight\meteo_db\ecmwf_ifs\20260523_12.nc")

output_folder = Path(r"D:\projects\Flood_Model\earth_sight\ht_meteo\png")
output_folder.mkdir(parents=True, exist_ok=True)

ds = xr.open_dataset(path)
print(ds["tp"])
print(ds["tp"].dims)
print(ds["tp"].shape)
print(ds["tp"].dtype)
var_name = "tp"
var = ds[var_name]

for i in range(len(ds.step)):
    fig, ax = plt.subplots(figsize=(10, 6))

    var.isel(step=i).plot(ax=ax)

    step_value = ds.step.values[i]
    ax.set_title(f"{var_name} - step {step_value}")

    output_path = output_folder / f"{var_name}_timestep_{i:03d}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")

    plt.close(fig)

ds.close()

print(f"Saved plots to: {output_folder}")