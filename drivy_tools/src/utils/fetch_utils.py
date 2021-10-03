import asyncio
from typing import List

from tqdm import tqdm

from drivy_tools.src.drivy_api import DrivyAPI
from drivy_tools.src.enums import brand_id_map, km_id_map, year_id_map
from drivy_tools.src.models import CityDetails
from drivy_tools.src.utils import save_csv
from drivy_tools.state import state


async def get_all_earnings(
    results_dir, drivy_api: DrivyAPI, city: CityDetails, brands_to_pass: List[str] = [], verbose: bool = True
):
    general_results = []
    brands_ids = list(brand_id_map.keys())
    for brand in brands_to_pass:
        brands_ids.remove(list(brand_id_map.keys())[list(brand_id_map.values()).index(brand)])

    if brands_to_pass:
        if verbose:
            print(f"Brands already fetched: {brands_to_pass}")

    brands_ids = brands_ids[:1]
    for brand_id in brands_ids:
        if verbose:
            print(f"Fetching for {brand_id_map.get(brand_id)} started..")
        brand_results = []
        try:
            models = await drivy_api.get_models(brand_id)
            await asyncio.sleep(state.config.DEFAULT.sleep_between_sec)
        except Exception as e:
            print(f"Model fetching didn't work for {brand_id_map.get(brand_id)}, detail {e}")
            continue
        with tqdm(total=len(models) * len(year_id_map) * len(km_id_map)) as pbar:
            for model in tqdm(models, desc=f"{brand_id_map.get(brand_id)}"):
                model_id = model.id
                for year_id in list(year_id_map.keys()):
                    for km_id in list(km_id_map.keys()):
                        try:
                            earning = await drivy_api.get_estimated_earning(brand_id, model_id, year_id, km_id, city)
                            pbar.update(1)
                        except Exception as e:
                            print(
                                f"Earning fetching didn't work for {brand_id_map.get(brand_id)}, {model.localized_label}, "
                                f"{year_id, km_id}, detail {e}"
                            )
                            continue
                        brand_results.append(
                            {
                                "brand": brand_id_map.get(brand_id),
                                "model": model.localized_label,
                                "year": year_id_map.get(year_id),
                                "km": km_id_map.get(km_id),
                                "earning": earning,
                            }
                        )
            if verbose:
                print(brand_results)
            save_csv(
                results_dir=results_dir,
                header=list(brand_results[0].keys()),
                results=brand_results,
                name_of_csv=brand_id_map.get(brand_id),
            )
        general_results.extend(brand_results)
    return general_results
