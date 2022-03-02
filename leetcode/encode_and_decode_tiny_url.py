import time

class Codec:

    code_urls = {}

    def encode(self, longUrl: str) -> str:
        hash_url = "%s-%s" % (time.time(), longUrl[-5:])
        self.code_urls[hash_url] = longUrl
        return hash_url

    def decode(self, shortUrl: str) -> str:
        return self.code_urls.get(shortUrl)

if __name__ == '__main__':
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    print(codec.decode(codec.encode(url)))
