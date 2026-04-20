import json
from services.aws import s3_service as s3_services
from services.aws import sqs_service as sqs_services
import uuid

global boletin_counter
boletin_counter = 0

# Definición de las funciones que manejan los boletines

def create_boletin_id():
    global boletin_counter
    boletin_id = str(str(uuid.uuid4()) + '-' + str(boletin_counter))
    boletin_counter += 1
    return boletin_id


def create_boletin(boletin_file: bytes, boletin_message: str, email: str):
    try:
        boletin_id = create_boletin_id()
        # Subimos el boletín a S3
        lint_to_s3 = s3_services.upload_file_to_s3(boletin_file, f'boletines/{email}/{boletin_id}.pdf')

        # Enviar un mensaje a SQS para notificar sobre el nuevo boletín
        message_body = {
            "boletin_id": boletin_id,
            "email": email,
            "message": boletin_message,
            "link_s3": lint_to_s3
        }
        json_message_body = json.dumps(message_body)
        sqs_services.send_message(json_message_body)

        return {"status": "success", "message": "Boletín creado y notificación enviada."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
