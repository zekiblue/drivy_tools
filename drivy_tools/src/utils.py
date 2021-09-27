import csv
from typing import List

from drivy_tools.src.drivy_api import DrivyAPI
from drivy_tools.src.enums import brand_id_map, km_id_map, year_id_map
from drivy_tools.src.models import CityDetails


async def get_all_earnings(
    drivy_api: DrivyAPI, city: CityDetails, brands_to_pass: List[str] = [], verbose: bool = True
):
    general_results = []
    brands_ids = list(brand_id_map.keys())
    for brand in brands_to_pass:
        brands_ids.remove(list(brand_id_map.keys())[list(brand_id_map.values()).index(brand)])

    if brands_to_pass:
        print(f"Brands already fetched: {brands_to_pass}")

    for brand_id in brands_ids:
        print(f"Fetching for {brand_id_map.get(brand_id)} started..")
        brand_results = []
        try:
            models = await drivy_api.get_models(brand_id)
        except Exception as e:
            print(f"Model fetching didn't work for {brand_id_map.get(brand_id)}, detail {e}")
            continue
        for model in models:
            model_id = model.id
            for year_id in list(year_id_map.keys()):
                for km_id in list(km_id_map.keys()):
                    try:
                        earning = await drivy_api.get_estimated_earning(brand_id, model_id, year_id, km_id, city)
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
            header=list(brand_results[0].keys()),
            results=brand_results,
            name_of_csv=brand_id_map.get(brand_id),
        )
        general_results.extend(brand_results)
    return general_results


def save_csv(*, header: List[str] = None, results: List[dict], name_of_csv: str):
    if not header:
        header = results[0].keys()

    directory = f"results/{name_of_csv}.csv"
    with open(directory, "w") as handle:
        dict_writer = csv.DictWriter(handle, header)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    print(f"Csv saved to the {directory}")
