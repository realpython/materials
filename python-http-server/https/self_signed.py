import tempfile
from dataclasses import dataclass
from pathlib import Path

from OpenSSL.crypto import (
    FILETYPE_PEM,
    TYPE_RSA,
    X509,
    PKey,
    dump_certificate,
    dump_privatekey,
)


@dataclass(frozen=True)
class SelfSignedCertificate:
    host: str = "0.0.0.0"
    bits: int = 2048
    country: str = "CA"
    state: str = "British Columbia"
    locality: str = "Vancouver"
    organization: str = "Real Python"
    organizational_unit: str = "Development"
    serial_number: int = 1
    expires_on: int = 365 * 24 * 60 * 60

    @property
    def path(self) -> Path:
        key_pair = PKey()
        key_pair.generate_key(TYPE_RSA, self.bits)

        certificate = X509()

        subject = certificate.get_subject()
        subject.CN = self.host
        subject.C = self.country
        subject.ST = self.state
        subject.L = self.locality
        subject.O = self.organization
        subject.OU = self.organizational_unit

        certificate.set_serial_number(self.serial_number)
        certificate.gmtime_adj_notBefore(0)
        certificate.gmtime_adj_notAfter(self.expires_on)
        certificate.set_issuer(subject)
        certificate.set_pubkey(key_pair)
        certificate.sign(key_pair, "sha256")

        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(dump_privatekey(FILETYPE_PEM, key_pair))
            file.write(dump_certificate(FILETYPE_PEM, certificate))

        return Path(file.name)
