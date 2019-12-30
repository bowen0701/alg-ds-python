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

class Codec:
    def __init__(self):
        import string
        from collections import defaultdict

        # Create base 62: a-zA-Z0-9.
        self.base = string.ascii_letters + ''.join([str(i) for i in range(10)])
        self.base_size = len(self.base)
        self.code2url = defaultdict(int)
        self.code_size = 6
        self.tiny_predix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # Hash by Folding method w/ sum of ordinal values plus mod base.
        ord_sum = 0
        for c in longUrl:
            ord_sum += ord(c)

        # TODO: Continue hashing and appending resulting char to code until hash equals 0.
        code = [self.tiny_predix]
        while ord_sum and len(code) < 1 + self.code_size:
            ord_sum, c = ord_sum // self.base_size, ord_sum % self.base_size
            code.append(c)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
