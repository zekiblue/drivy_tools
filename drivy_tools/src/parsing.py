def parse_text_to_earning(text):
    earning = None
    if "car_model_estimation_result_amount" in text:
        earning = text.split('"car_model_estimation_result_amount\\">€')[1]
        earning = earning.split("</span")[0].strip()
    return earning
