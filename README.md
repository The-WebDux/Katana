# Katana -)====>

- პროგრამას შეუძლია გატეხოს, დააგენერიროს ან ამოიცნოს ჰეშები

- გატეხვის მეთოდები: ონლაინ ბაზები, ბრუტფორსი

- ხელმისაწვდომი ჰეშის ტიპები: md5, sha1, sha224, sha256, sha384, sha512

# ინსტალაცია
```bash
$ git clone https://github.com/vakh0/Katana
$ cd Katana
$ pip install -r requirements.txt
$ sudo chmod +x katana.py
$ sudo mv katana.py /usr/bin/katana
```

# ინსტრუქცია
```bash
# გამოყენების ინსტრუქციის ჩვენება
$ katana --help

# მენიუს გახსნა (ინტერაქტიული გარემო)
$ katana -m

# გატეხოს md5 ტიპის ჰეში, ჯერ შეამოწმებს ონლაინ ბაზებში შემდეგ დაიწყებს Bruteforce-ს
$ katana.py -t md5 --string 25fcbcf7a396f06d947e11bcbb5217a1 --min 4 --max 6 -l 1 --online
```


# სქრინები
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-18-11.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-19-09.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-19-20.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-24-26.png)
