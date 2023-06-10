enc_word_1 = "разработка"
enc_word_1_bytes = enc_word_1.encode('utf-8')
print(enc_word_1_bytes)

enc_word_1_bytes = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
enc_word_1 = enc_word_1_bytes.decode('utf-8')
print(enc_word_1)
print("-"*50)

enc_word_2 = "администрирование"
enc_word_2_bytes = enc_word_2.encode('utf-8')
print(enc_word_2_bytes)

enc_word_2_bytes = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
enc_word_2 = enc_word_2_bytes.decode('utf-8')
print(enc_word_2)
print("-"*50)

enc_word_3 = "protocol"
enc_word_3_bytes = enc_word_3.encode('utf-8')
print(enc_word_3_bytes)

enc_word_3_bytes = b'protocol'
enc_word_3 = enc_word_3_bytes.decode('utf-8')
print(enc_word_3)
print("-"*50)

enc_word_4 = "standard"
enc_word_4_bytes = enc_word_4.encode('utf-8')
print(enc_word_4_bytes)

enc_word_4_bytes = b'standard'
enc_word_4 = enc_word_4_bytes.decode('utf-8')
print(enc_word_4)
