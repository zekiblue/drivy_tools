from drivy_business.src.drivy_api import DrivyAPI
from drivy_business.src.enums import brand_id_map, year_id_map, km_id_map
from drivy_business.src.models import CityDetails


async def get_all_earnings(drivy_api: DrivyAPI, city: CityDetails):
    results = []
    for brand_id in list(brand_id_map.keys()):
        models = await drivy_api.get_models(brand_id)
        for model in models:
            model_id = model.id
            for year_id in list(year_id_map.keys()):
                for km_id in list(km_id_map.keys()):
                    earning = await drivy_api.get_estimated_earning(brand_id, model_id, year_id, km_id, city)
                    results.append(
                        {
                            "brand": brand_id_map.get(brand_id),
                            "model": model.localized_label,
                            "year": year_id_map.get(year_id),
                            "km": km_id_map.get(km_id),
                            "earning": earning
                        }
                    )
        print(results)
        break
