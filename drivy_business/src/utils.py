import csv
from typing import List

from drivy_business.src.drivy_api import DrivyAPI
from drivy_business.src.enums import brand_id_map, year_id_map, km_id_map
from drivy_business.src.models import CityDetails


async def get_all_earnings(drivy_api: DrivyAPI, city: CityDetails, verbose: bool = True):
    general_results = []
    for brand_id in list(brand_id_map.keys()):
        brand_results = []
        models = await drivy_api.get_models(brand_id)
        for model in models:
            model_id = model.id
            for year_id in list(year_id_map.keys()):
                for km_id in list(km_id_map.keys()):
                    earning = await drivy_api.get_estimated_earning(brand_id, model_id, year_id, km_id, city)
                    brand_results.append(
                        {
                            "brand": brand_id_map.get(brand_id),
                            "model": model.localized_label,
                            "year": year_id_map.get(year_id),
                            "km": km_id_map.get(km_id),
                            "earning": earning
                        }
                    )
        if verbose:
            print(brand_results)
        save_csv(header=list(brand_results[0].keys()), results=brand_results, name_of_csv=brand_id_map.get(brand_id))
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
