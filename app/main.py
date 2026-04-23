import os
import time
from scraper import TransparencyAPI, N8nIntegration
from dotenv import load_dotenv

load_dotenv()

BASE_URL_API = os.getenv("BASE_URL_API", "https://dadosabertos.camara.leg.br/api/v2")
N8N_WEBHOOK = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook-test/df2de181-7ade-4305-8878-84a52b9d4d61")

def run():
    api = TransparencyAPI(BASE_URL_API)
    n8n = N8nIntegration(N8N_WEBHOOK)

    datasets = api.get_datasets(pagina=1)

    if datasets:
        payload = {
            "origem": "Python_Scraper_Legislativo",
            "total_datasets": len(datasets),
            "data": datasets 
        }

        n8n.send_data(payload)
    else:
        print("Nenhum dado encontrado para enviar.")

if __name__ == "__main__":
    run()