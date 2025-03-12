from mnemonic import Mnemonic

mnemo = Mnemonic("english")
seed_phrase = mnemo.generate(strength=192)  # 192-bit entropy برای 18 کلمه
print(seed_phrase)
