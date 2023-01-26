import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad

# class AES256():
    
#     def __init__(self):
#         self.BS=16
#         self.pad=lambda s:s+(self.BS-len(s.encode('utf-8'))%self.BS)*chr(self.BS-len(s.encode('utf-8'))%self.BS)
#         self.unpad=lambda s :s[0:-s[-1]]
#         self.key=hashlib.sha256().digest()
    
#     def encrypt(self,raw):
#         raw=self.pad(raw)
#         iv=Random.new().read(AES.block_size)
#         cipher=AES.new(self.key,AES.MODE_CFB,iv)
#         return base64.b64encode(iv+cipher.encrypt(raw.encode('utf-8')))

#     def decrypt(self,enc):
#         enc=base64,base64.b64decode(enc)
#         iv=enc[:16]
#         cipher=AES.new(self.key,AES.MODE_CFB,iv)
#         return self.unpad(cipher.decrypt(enc[16:]))
    
#     def encrypt_str(self,raw):
#         return self.encrypt(raw).decode('utf-8')
    
#     def decrypt_str(self,enc):
#         if type(enc)==str:
#             enc=str.encode(enc)
#             return self.decrypt(enc).decode('utf-8')
class AES256():

    def __init__(self, key):
        self.bs = 16
        self.key = key.encode('utf-8')
        self.key = AES256.str_to_bytes(key)

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AES256.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        print("1")
        print(self)
        raw = self._pad(AES256.str_to_bytes(raw))
        print(raw)
        iv = Random.new().read(AES.block_size)
        print(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        print(cipher)
        result = iv.encode('utf-8') + cipher.encrypt(raw.decode('utf-8'))
        return base64.b64encode(result)

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')