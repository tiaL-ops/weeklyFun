import string


BASE62_CHARS = string.ascii_letters + string.digits  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


url_mapping = {}
counter = 1  

def encode_base62(num):

    if num == 0:
        return BASE62_CHARS[0]
    
    base62_str = ""
    while num:
        num, remainder = divmod(num, 62)
        base62_str = BASE62_CHARS[remainder] + base62_str
    return base62_str

def decode_base62(base62_str):
  
    num = 0
    for char in base62_str:
        num = num * 62 + BASE62_CHARS.index(char)
    return num

def shorten_url(long_url):
   
    global counter
    
    short_code = encode_base62(counter)
    url_mapping[short_code] = long_url  # Store mapping
    
    counter += 1  # Increment counter for uniqueness
    
    return f"http://short.url/{short_code}"

def get_original_url(short_code):
   
    return url_mapping.get(short_code, "URL not found")


if __name__ == "__main__":
    long_url = input("URl ")
    short_url = shorten_url(long_url)
    print(f"Short URL: {short_url}")

    
    short_code = short_url.split("/")[-1]
    original_url = get_original_url(short_code)
    print(f"Original URL: {original_url}")
