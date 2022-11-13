# Katana -)======>

- პროგრამას შეუძლია გატეხოს, დააგენერიროს ან ამოიცნოს ჰეშები

- ხელმისაწვდომი შეტევის ტიპები: Bruteforce, Wordlist, Custom Keywords, Online Databases

- ხელმისაწვდომი ალგორითმები: md5, sha1, sha224, sha256, sha384, sha512

# ინსტალაცია
```bash
$ git clone https://github.com/vakh0/Katana
$ cd Katana
$ pip install -r requirements.txt
$ sudo chmod +x katana.py
$ sudo mv katana.py /usr/bin/katana
$ katana
```

# ინსტრუქცია
```
# მენიუს გამოძახება - ინტერაქტიული გარემო
$ katana -m

# ონლაინ ბაზებში შემოწმება + ბრუტფორსი
$ katana --type md5 --string 23b4222d2613a2765d4d432d2d65e88e --min 4 --max 6 --list 1 --online

# ვორდლისტით გატეხვა
$ katana --type md5 --string 23b4222d2613a2765d4d432d2d65e88e --wordlist /usr/share/wordlists/rockyou.txt

# -m ან --menu იძახებს მენიუს
# -t ან --type ჰეშის ტიპი/ალგორითმი
# -s ან --string გასაშიფრი/დასაშიფრი ტექსტი
# --min ბრუტფორსისთვის ტექსტის მინიმალური სიგრძე
# --max ბრუტფორსისთვის ტექსტის მაქსიმალური სიგრძე
# --list სიმბოლოების ნაკრები (იხილე მენიუში ან გამოიყენე --keyword)
# -k ან --keyword ბრუტფორსში შენს მიერ შეყვანილი სიმბოლოების/ასოების გამოყენება
# -w ან --wordlist ბრუტფორსისთვის წინასწარ შედგენილი ლექსიკონის ფაილის გამოყენება
# -o ან --online ჰეშის ონლაინ მონაცემთა ბაზაში შემოწმება (მხოლოდ md5)
# --quiet ან -q ჩუმი რეჟიმი (მეტი სიჩქარისთვის)
# -h ან --help ინსტრუქციის ნახვა
```

# სქრინები

![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-18-11.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-19-09.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-19-20.png)
![](https://github.com/vakh0/Screenshots/blob/main/Katana/Screenshot%20from%202022-10-16%2017-24-26.png)
