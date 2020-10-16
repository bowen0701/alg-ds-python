"""Leetcode 535. Encode and Decode TinyURL
Medium

URL: https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System Design problem: Design TinyURL:
https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/

TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no
restriction on how your encode/decode algorithm should work. You just need to
ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL.

Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode(url))
"""

class CodecRandom:
    def __init__(self):
        import string
        from collections import defaultdict

        # Create base 62: a-zA-Z0-9.
        self.base = string.ascii_letters + ''.join([str(i) for i in range(10)])
        self.base_size = len(self.base)
        self.code_size = 6
        self.code2urls = defaultdict(int)
        self.url2codes = defaultdict(int)
        self.tiny_predix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import random

        # Continue randomly selecting 6 chars from base until get new code.
        while longUrl not in self.url2codes:
            code = ''.join(random.choice(self.base) for _ in range(self.code_size))
            if code not in self.code2urls:
                self.code2urls[code] = longUrl
                self.url2codes[longUrl] = code

        return self.tiny_predix + self.url2codes[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl.split('/')[-1]
        return self.code2urls[code]


class CodecHash:
    def __init__(self):
        import string
        from collections import defaultdict

        # Create base 62: a-zA-Z0-9.
        self.base = string.ascii_letters + ''.join([str(i) for i in range(10)])
        self.base_size = len(self.base)
        self.code_size = 6
        self.code2urls = defaultdict(int)
        self.tiny_predix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # Hash by Folding method w/ weighted sum of ordinal values with mod.
        ord_sum = 0
        for w, c in enumerate(longUrl):
            ord_sum += w * ord(c)

        # Continue hashing and appending resulting char to code until hash equals 0.
        codes = []
        while ord_sum and len(codes) < self.code_size:
            ord_sum, c = ord_sum // self.base_size, ord_sum % self.base_size
            codes.append(self.base[c])
        code = ''.join(codes)

        self.code2urls[code] = longUrl
        return self.tiny_predix + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl.split('/')[-1]
        return self.code2urls[code]


def main():
    longUrl = 'https://leetcode.com/problems/design-tinyurl'

    codec = CodecRandom()
    shortUrl = codec.encode(longUrl)
    print shortUrl
    print codec.decode(shortUrl)

    codec = CodecHash()
    shortUrl = codec.encode(longUrl)
    print shortUrl
    print codec.decode(shortUrl)


if __name__ == '__main__':
    main()
