from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/configMap")
def get_config():
    config_value = os.getenv("APP_CONFIG_KEY", "Config value not found")
    config_value_2 = os.getenv("APP_CONFIG_KEY_2", "Config value not found")
    config_value_3 = os.getenv("APP_CONFIG_KEY_3", "Config value not found")
    return {
        "config_value": config_value,
        "config_value_2": config_value_2,
        "config_value_3": config_value_3,
    }


@app.get("/secret")
def get_config():
    secret_value = os.getenv("SECRET_KEY", "Secret not found")
    secret_value_2 = os.getenv("SECRET_KEY_2", "Secret not found")
    return {
        "secret_value": secret_value,
        "secret_value_2": secret_value_2,
    }