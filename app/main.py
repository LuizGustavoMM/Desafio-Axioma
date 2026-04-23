import os
from app.scraper import TransparencyAPI, N8nIntegration
from dotenv import load_dotenv

load_dotenv()

BASE_URL_API = "URL_DA_API_AQUI"
N8N_WEBHOOK = os.getenv("N8N_WEBHOOK_URL")

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