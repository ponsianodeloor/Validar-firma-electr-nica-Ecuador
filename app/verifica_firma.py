import base64
import requests
from requests.exceptions import ConnectTimeout

if __name__ == "__main__":
    header = {"Content-Type": "text/plain; charset=UTF-8"}
    WS_VALIDACION_FIRMA_MINTEL = (
        "https://ws.firmadigital.gob.ec/servicio/validacionavanzadapdf"
    )

    with open("signed.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())

    try:
        response_backup = requests.post(
            url=WS_VALIDACION_FIRMA_MINTEL,
            data=encoded_string.decode("utf-8"),
            headers=header,
        )
        print(response_backup.text)
    except ConnectTimeout as err:
        print("Request has timed out WS_FIRMA_MINTEL")
        print(f"Unexpected {err=}, {type(err)=}")
    except Exception as err:
        print("Error requesting WS_FIRMA_SERCOP")
        print(f"Unexpected {err=}, {type(err)=}")
