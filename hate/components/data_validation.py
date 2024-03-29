import hashlib

def calculate_md5(filename, block_size=65536):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hash_md5.update(block)
    print(hash_md5.hexdigest())
    return hash_md5.hexdigest()

calculate_md5(r'C:\Users\furkanbaba\Desktop\furkanbaba\coding\NLP-PROJECT\artifacts\03_28_2024_21_28_08\DataIngestionArtifacts\data.zip')
