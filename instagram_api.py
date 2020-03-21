import hashlib
import string
import random

from instagram_web_api import Client


__all__ = ('instagram_web_api_client',)


class InstagramClient(Client):

    @staticmethod
    def _extract_rhx_gis(html):
        options = string.ascii_lowercase + string.digits
        text = ''.join([random.choice(options) for _ in range(8)])
        return hashlib.md5(text.encode()).hexdigest()


instagram_web_api_client = InstagramClient(auto_patch=True, drop_incompat_keys=False)
