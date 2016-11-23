import hashlib
import hmac
from urllib.parse import urlsplit


def generate_signature(method, version, endpoint,
                       date, request_path, content,
                       access_key, secret_key, hash_type):
    '''
    Generates the API request signature from the given parameters.
    '''
    hash_type = hash_type
    hostname = urlsplit(endpoint).netloc
    body_hash = hashlib.new(hash_type, content).hexdigest()
    major_ver = version.split('.', 1)[0]

    sign_str = '{}\n/{}/{}\n{}\nhost:{}\ncontent-type:application/json\nx-sorna-version:{}\n{}'.format(
        method.upper(),
        major_ver, request_path,
        date.isoformat(),
        hostname,
        version,
        body_hash
    )
    sign_bytes = sign_str.encode()

    sign_key = hmac.new(secret_key.encode(),
                        date.strftime('%Y%m%d').encode(), hash_type).digest()
    sign_key = hmac.new(sign_key, hostname.encode(), hash_type).digest()

    signature = hmac.new(sign_key, sign_bytes, hash_type).hexdigest()
    headers = {
        'Authorization': 'Sorna signMethod=HMAC-{}, credential={}:{}'.format(
            hash_type.upper(),
            access_key,
            signature
        ),
    }
    return headers, signature
