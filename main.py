import json
import qrcode
import os

from twofas_lib import QRCode

def generate_qr_codes(file_path):
    # Create output directory if it doesn't exist
    output_dir = "qr_codes"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load json file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Parse json file and generate QR codes for each service
    for service in data["services"]:
        # Generate QrCode object
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
            
            # Generate QR code based on QrCode OTPAuth URL
            qr_img = qrcode.make(qr_code.otpauth)
            output_file = os.path.join(output_dir, f"{qr_code.issuer}.png")
            qr_img.save(output_file)

            print(f"QRCode {qr_code.label} saved as {output_file}")
            
        except KeyError:
            print(f"JSON file for {service['otp']['label']} is not properly formatted or a value is missing")
                 
#Generate QR codes for 2fastest.json
generate_qr_codes(".env/2fastest.json")