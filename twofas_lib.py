class QRCode:
    def __init__(self, issuer="", secret="", account="", digits="6", period="", algorithm="SHA1", tokenType="TOTP"):
        self.issuer = issuer                # Account issuer
        self.tokenType= tokenType           # TOTP or HOTP
        self.secret = secret                # Base32 encoded secret
        self.account = account              # Account email or username

        self.digits = digits                # Number of digits in the code (6 or 8)
        self.period = period                # Time period in seconds (default 30)
        self.algorithm = algorithm          # Hash algorithm (SHA1, SHA256, SHA512) (default SHA1)
       
        self.label = f"{issuer}:{account}"  # Account name / Account issuer @ Account email or username
        self.otpauth = f"otpauth://{self.tokenType}/{self.label}?secret={self.secret}&issuer={self.issuer}&digits={self.digits}&period={self.period}&algorithm={self.algorithm}"
    