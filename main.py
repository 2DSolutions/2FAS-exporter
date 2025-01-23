import json
import qrcode
import os

from twofas_lib import QRCode

def generate_qr_codes(file_path):
    # Crée un dossier pour sauvegarder les QR codes
    output_dir = "qr_codes"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Charge le fichier JSON
    with open(file_path, "r") as file:
        data = json.load(file)

    # Parcourt chaque service dans le fichier JSON
    for service in data["services"]:
        # Crée un objet QRCode
        
        try:
            qr_code = QRCode(
                    secret=service["secret"],
                    issuer=service["otp"]["issuer"],
                    tokenType=service["otp"]["tokenType"],
                    digits=service["otp"]["digits"] if "digits" in service["otp"] else "6",
                    period=service["otp"]["period"] if "period" in service["otp"] else "",
                    algorithm=service["otp"]["algorithm"] if "algorithm" in service["otp"] else "SHA1",
                    account=service["otp"]["account"],
                    )
            
            qr_img = qrcode.make(qr_code.otpauth)
            output_file = os.path.join(output_dir, f"{qr_code.issuer}.png")
            qr_img.save(output_file)

            print(f"QR Code pour {qr_code.label} sauvegardé sous {output_file}")
            
        except KeyError:
            print(f"Le fichier JSON pour {service["otp"]["label"]}n'est pas correctement formaté ou une valeur est manquante")
            
            


# Exemple d'utilisation
generate_qr_codes(".env/2fastest.json")