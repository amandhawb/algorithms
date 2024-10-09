# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:

# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

class Solution:
    def __init__(self): 
        self.encode_map = {}
        self.decode_map = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_map:
            short_url = self.base_url + str(len(self.encode_map))
            self.encode_map[longUrl] = short_url
            self.decode_map[short_url] = longUrl
        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decode_map[shortUrl]

# TEST 1
solution = Solution()
long_url = "https://www.example.com"
short_url = solution.encode(long_url)
decoded_url = solution.decode(short_url)
assert long_url == decoded_url
    
# TEST 2
solution = Solution()
urls = ["https://www.example1.com", "https://www.example2.com", "https://www.example3.com"]
short_urls = [solution.encode(url) for url in urls]
decoded_urls = [solution.decode(short_url) for short_url in short_urls]
assert urls == decoded_urls

