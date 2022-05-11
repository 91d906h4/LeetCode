import hashlib
class Codec:
    def __init__(self):
        self.url ={}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
#         return longUrl

        hash_key =  "https://url.co/".join(hashlib.sha256(longUrl.encode()).hexdigest())
        self.url[hash_key] = longUrl
        return hash_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
#         return shortUrl

        return self.url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
