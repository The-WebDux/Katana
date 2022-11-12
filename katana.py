#!/usr/bin/python3
# Coded by - WebDux -

import argparse
from termcolor import colored
from printy import printy
import hashlib, os, time, sys, itertools
import requests
import re
from colorama import Fore, Back, Style, init
init()

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
purple = Fore.MAGENTA
white = Fore.WHITE
yellow = Fore.YELLOW
backRed = Back.RED
backBlack = Back.BLACK
endStyle = Style.RESET_ALL

list1 = ' abcdefghijklmnopqrstuvwxyz'
list2 = ' abcdefghijklmnopqrstuvwxyz0123456789'
list3 = ' abcdefghijklmnopqrstuvwxyz[]{}"!@#$%^&*().,/;'
list4 = ' abcdefghijklmnopqrstuvwxyz0123456789[]{}"!@#$%^&*().,/;'
list5 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
list6 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ0123456789'
list7 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ[]{}"!@#$%^&*().,/;'
list8 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ0123456789[]{}"!@#$%^&*().,/;'
customList = []

hashMethods = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

banerParameter = {"Allow" : True}
quietParameter = {"Allow" : False}

def banner():
	printy("\n --- Welcome to Katana --- ", "rBU")


def dictionary(location, hashMethod, string):
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	try:
		with open(location, 'r', encoding='utf-8') as wordlist:
			wordlist.close()
	except:
		print(f"\n {backRed}{white}[!]{endStyle}{backBlack}{red} ვორდლისტის {yellow}ლოკაცია {red}არასწორად არის მითითებული ან კითხვის {yellow}უფლება {red}არ მაქვს{endStyle}")
		sys.exit()

	count = 0
	with open (location, 'r') as wordlist:
		global success
		success = False
		startTime = time.time()
		print()
		for word in wordlist:

			match hashMethod:
				case "md5":
					resultHash = hashlib.md5(word.strip().encode())
					shifri = resultHash.hexdigest()
				case "sha1":
					resultHash = hashlib.sha1(word.strip().encode())
					shifri = resultHash.hexdigest()	
				case "sha224":
					resultHash = hashlib.sha224(word.strip().encode())
					shifri = resultHash.hexdigest()	
				case "sha256":
					resultHash = hashlib.sha256(word.strip().encode())
					shifri = resultHash.hexdigest()		
				case "sha384":
					resultHash = hashlib.sha384(word.strip().encode())
					shifri = resultHash.hexdigest()	
				case "sha512":
					resultHash = hashlib.sha512(word.strip().encode())
					shifri = resultHash.hexdigest()

			count += 1
			usingWord = word.join("")
			sys.stdout.write(f"\r{yellow} [+] შემოწმებული ლაინი | {red}{count}\r")
			sys.stdout.flush()
			result_MD5 = hashlib.md5(word.strip().encode())
			if string in shifri:
				endTime = time.time()
				timeNOW = endTime - startTime
				print(f"\r\n{yellow} [+] 	 	   დრო | {purple}{timeNOW} წამი")
				print(f"{yellow} [+]   მოწოდებული ჰეში | {blue}{shifri}")
				print(f"{green} [+]   	        ტექსტი {yellow}| {green}{word}\r")
				success = True
				sys.exit()
		if not success:
			print(f"\n {backRed}{white}[!]{endStyle}{red} ჰეში ამ ვორდლისტიდან ვერ გაიშიფრა, სცადე სხვა მეთოდი")

def onlineDatabase(hash, type):
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	if type != "md5":
		print(f"\n {backRed}{white}[!]{endStyle}{red}{backBlack} ონლაინ ბაზებში მოწმდება მხოლოდ {yellow} MD5{endStyle}")
		sys.exit()
	print(f"\n{backBlack} {white}[{green}INFO{white}] ვამოწმებ ონლაინ ბაზებში{endStyle}")
	s = requests.Session()
	data_payload = {'87':'', 'decrypt':'Decrypt', 'hash':hash}
	response = s.post('https://md5decrypt.net/en/', data=data_payload, allow_redirects=True, timeout=30)
	op = re.compile(r'</script></span></span><br>'+hash+' : <b>(.*?)</b><br><br>Found').findall(response.text)
	if response.status_code != 200:
		print(f" {backRed}{white}[!]{endStyle}{red}ვერ დავუკავშირდი სერვერს", response.status_code)		
	elif "Found" not in response.text or op==[]:
		s.cookies.clear()
	else:
		print(f"\n{yellow} [+] ჰეში ნაპოვნია: {green}{op[0]}")
		s.cookies.clear()
		sys.exit()
	
	s = requests.Session()
	header_payload={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',}
	response = s.get('https://hashtoolkit.com/decrypt-hash?hash='+hash, headers=header_payload, allow_redirects=True, timeout=30)
	op1 = re.compile(r'title="decrypted md5 hash">(.*?)</span>').findall(response.text)
	try:
		op = re.compile(r'>(.*?)<').findall(op1[0])
		print(f"\n{yellow} [+] ჰეში ნაპოვნია: {green}{op[0]}")
		sys.exit()		
	except:
		pass

	if response.status_code!=200:
		print(f"{red} ვერ დავუკავშირდი სერვერს",response.status_code)
	elif "No hashes found" in response.text or op==[]:
		print(f" {backBlack}{white}[{red}-{white}] ვერ ვიპოვე{endStyle}")
		s.cookies.clear()
	else:
		print(f"\n{yellow} [+] ჰეში ნაპოვნია: {green}{op[0]}")
		s.cookies.clear()
		sys.exit()

def decrypt(hashMethod, string, minLenght, maxLenght, listChoice, online=None):
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	if online:
		try:
			onlineDatabase(string, hashMethod)
		except requests.exceptions.ConnectionError:
			print(f" {backRed}{white}[!]{endStyle}{red} ონლაინ ბაზებში შესამოწმებლად საჭიროა ინტერნეტი")
		except KeyboardInterrupt:
			print(f" {backRed}{white}[!]{endStyle}{red}{backBlack} ონლაინ ბაზებში შემოწმება ძალით გაჩერდა{endStyle}")
			sys.exit()
	print(f"\n{Back.BLACK} {white}[{green}INFO{white}] ვიწყებ ბრუტფორსს{endStyle}")
	success = False
	datvla = 0
	maxLenght = maxLenght + 1
	if listChoice == 1:
		usingList = list1
	if listChoice == 2:
		usingList = list2
	if listChoice == 3:
		usingList = list3
	if listChoice == 4:
		usingList = list4
	if listChoice == 5:
		usingList = list5
	if listChoice == 6:
		usingList = list6
	if listChoice == 7:
		usingList = list7
	if listChoice == 8:
		usingList = list8
	if listChoice == 0: # ai aq
		usingList = str(customList)


	if quietParameter["Allow"] == False:
		startTime = time.time()
		sys.stdout.write(f"\n {yellow}[+]      პარამეტრები: | ტიპი: {purple}{hashMethod}{yellow} ლექსიკონი: {purple}{listChoice}{yellow} სიმბოლო: {purple}{minLenght} - {maxLenght-1}\n")
		sys.stdout.flush()
		print(f" {yellow}[+] დაშიფრული ტექსტი: |{blue} {string} {yellow}|")
		startTime = time.time()
		for n in range(minLenght, maxLenght):
			for xs in itertools.product(usingList, repeat=n):
				endTime = time.time()
				timeNOW = endTime - startTime
				datvla += 1
				match hashMethod:
					case "md5":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.md5(Generated.encode())
						shifri = resultHash.hexdigest()
					case "sha1":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha1(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha224":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha224(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha256":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha256(Generated.encode())
						shifri = resultHash.hexdigest()		
					case "sha384":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha384(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha512":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha512(Generated.encode())
						shifri = resultHash.hexdigest()
				if not success:	
					sys.stdout.write(f"\r {yellow}[+]     ვიყენებ ჰეშს: | {red}{shifri}{yellow} |\r")
					sys.stdout.flush()
				if string == shifri:
					sys.stdout.write(f"\r {yellow}[+]     ვიყენებ ჰეშს: | {blue}{shifri}{yellow} \n")
					print(f" [+]           შედეგი: | მცდელობა: {purple}{datvla}{yellow} - დრო: {purple}{timeNOW} წამი")
					print(f" {green}[+]           ტექსტი: {yellow}| {green}{Generated} ")
					success = True
					break
		if not success:
			sys.stdout.write(f"\r {yellow}[-]     ვიყენებ ჰეშს: | {red}{shifri}{yellow} |")
			print(f"\r {yellow}[-]        რესურსები: | მცდელობა: {purple}{datvla}{yellow} - დრო: {purple}{timeNOW} წამი")
			print(f" {red}[!]           ტექსტი: {yellow}| {backRed}{white}ვერ გაიშიფრა{white}{endStyle}")
			print(f"\n {backRed}{white}[!]{endStyle}{yellow} ჰეში {red}ვერ {yellow}გაიშიფრა, სცადე {red}სხვა პარამეტრები")

	else:
		print(f"\n{backBlack} {white}[{green}INFO{white}] მიმდინარეობს ბრუტფორსი ჩუმ რეჟიმში, დაელოდე დასრულებას{endStyle}")
		startTime = time.time()
		for n in range(minLenght, maxLenght):
			for xs in itertools.product(usingList, repeat=n):
				endTime = time.time()
				timeNOW = endTime - startTime
				datvla += 1
				match hashMethod:
					case "md5":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.md5(Generated.encode())
						shifri = resultHash.hexdigest()
					case "sha1":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha1(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha224":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha224(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha256":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha256(Generated.encode())
						shifri = resultHash.hexdigest()		
					case "sha384":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha384(Generated.encode())
						shifri = resultHash.hexdigest()	
					case "sha512":
						Generated = ''.join(map(str, xs)) 
						resultHash = hashlib.sha512(Generated.encode())
						shifri = resultHash.hexdigest()
				if not success:	
					pass
				if string == shifri:
					print(f"\n {backBlack}{green}გაშიფვრა დასრულებულია. {blue}{endStyle}")
					print(f"\n {yellow}[+]      პარამეტრები: | ტიპი: {purple}{hashMethod}{yellow} ლექსიკონი: {purple}{listChoice}{yellow} სიმბოლო: {purple}{minLenght} - {maxLenght-1}")
					print(f" {yellow}[+]           შედეგი: | მცდელობა: {purple}{datvla}{green} - დრო: {purple}{timeNOW} წამი")
					print(f" {yellow}[+]   გასაშიფრი ჰეში: | {blue}{shifri}")
					print(f" {yellow}[+]           ტექსტი: {yellow}| {green}{Generated} ")
					success = True
					break
		if not success:
			print(f"\n {backRed}{white}[!]{endStyle}{yellow} ჰეში {red}ვერ {yellow}გაიშიფრა, სცადე {red}სხვა პარამეტრები")
			print(f"\n {white}[{red}-{white}]{white} მცდელობა: {purple}{datvla}{white} - დრო: {purple}{timeNOW} {white}წამი")


def menu():
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	print(f"{yellow}\n [1] დაშიფვრა")
	print(f"{yellow} [2] გაშიფვრა")
	print(f"{yellow} [3] ანალიზი")
	choice = input(f"{yellow}\n[?]- ")

	if choice == "1":
		print(f"{red}- მეთოდები -\nmd5, sha1, sha224, sha256, sha384, sha512")
		hashMethod = input(f"{yellow}[?] ჰეშირების მეთოდი: {white}")
		string = input(f"{yellow}[?] ტექსტი: {white}")
		crypt(string, hashMethod)
	elif choice == "2":

		print(f"{red}- მეთოდები -\nmd5, sha1, sha224, sha256, sha384, sha512")
		hashMethod = input(f"{yellow} [?] ჰეშირების მეთოდი: ")
		if hashMethod not in hashMethods:
			print(f"\n {backRed}{white}[!]{endStyle}{red} ჰეშირების {yellow}ტიპი{red}/{yellow}მეთოდი{red} არასწორად გაქვს მითითებული. გამოიყენე {yellow}--help {red}ან {yellow}--menu")
			sys.exit()
		string = input(f"{yellow} [?] დაშიფრული ტექსტი: ")
		if hashMethod == "md5":
			try:
				onlineDatabase(string, hashMethod)
			except requests.exceptions.ConnectionError:
				print(f"{backRed}{white}[!]{endStyle}{red} ონლაინ ბაზებში შესამოწმებლად საჭიროა ინტერნეტი")
				sys.exit()
			except KeyboardInterrupt:
				print(f" {backRed}{white}[!]{endStyle}{red} ონლაინ ბაზებში შემოწმება ძალით შეჩერდა")
				sys.exit()
		minLenght = int(input(f"{yellow} [?] ტექსტის მინიმალური სიგრძე: "))
		maxLenght = int(input(f"{yellow} [?] ტექსტის მაქსიმალური სიგრძე: "))
		print(f"\n{red}-[ სიმბოლოების ნაკრები ]-\n{blue}1: {list1}\n2: {list2}\n3: {list3}\n4: {list4}\n5: {list5}\n6: {list6}\n7: {list7}\n8: {list8}\n")
		selectedList = int(input(f"{yellow} [!]: აირჩიე სიმბოლოების ნაკრები: "))
		
		match hashMethod:
			case "md5":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case "sha1":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case "sha224":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case "sha256":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case "sha384":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case "sha512":
				decrypt(hashMethod, string, minLenght, maxLenght, selectedList, online=False)
			case _:
				print(f"{backRed}[!]{endStyle}{red} მიუთითე ჩამოთვლილიდან რომელიმე")
	elif choice == "3":
		string = input(f"{backRed}[!]{endStyle}{green} შეიყვანე დაშიფრული ტექსტი: ")
		os.system("hashid " + string)


def crypt(string, hashMethod):
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	if hashMethod not in hashMethods:
		print(f"\n {backRed}{white}[!]{endStyle}{red} ჰეშირების {yellow}ტიპი{red}/{yellow}მეთოდი{red} არასწორად გაქვს მითითებული. გამოიყენე {yellow}--help {red}ან {yellow}--menu")
		sys.exit()
	match hashMethod:
		case "md5":
			result_MD5 = hashlib.md5(string.encode())
			print(purple,"\nMD5: ", blue, result_MD5.hexdigest())
		case "sha1":
			result_SHA1 = hashlib.sha1(string.encode())
			print(purple,"\nsha1: ", blue, result_SHA1.hexdigest())
		case "sha224":
			result_SHA224 = hashlib.sha224(string.encode())
			print(purple,"\nsha224: ", blue, result_SHA224.hexdigest())
		case "sha256":
			result_SHA256 = hashlib.sha256(string.encode())
			print(purple,"\nsha256: ", blue, result_SHA256.hexdigest())
		case "sha384":
			result_SHA384 = hashlib.sha384(string.encode())
			print(purple,"\nsha384: ", blue, result_SHA384.hexdigest())
		case "sha512":
			result_SHA512 = hashlib.sha512(string.encode())
			print(purple,"\nsha512: ", blue, result_SHA512.hexdigest())
	

if __name__ == "__main__":
	if banerParameter["Allow"] == True:
		banerParameter["Allow"] = False
		banner()
	parser = argparse.ArgumentParser()
	parser.add_argument('-m','--menu', action='store_true', help='ინტერაქტიული მენიუ')
	parser.add_argument('-o','--online', action='store_true', help='MD5 ონლაინ ბაზებში შემოწმება')
	parser.add_argument('-t','--type', metavar='type', type=str, help='ჰეშის ტიპი')
	parser.add_argument('-s', '--string', metavar='', type=str, help='გასაშიფრი/დასაშიფრი ტექსტი')
	parser.add_argument('--min', metavar='minLenght', type=int, help='მინიმალური სიგრძე')
	parser.add_argument('--max', metavar='maxLenght', type=int, help='მაქსიმალური სიგრძე')
	parser.add_argument('-l','--list', metavar='list', type=int, help='ლექსიკონი')
	parser.add_argument('-w','--wordlist', metavar='wordlist.txt', help='ლექსიკონი')
	parser.add_argument('-k','--keyword', metavar='abcdefg...' , help='პირადი ლექსიკონი')
	parser.add_argument('-q','--quiet', action='store_true', help='ჩუმი რეჟიმი (ჩქარი)')
	args = parser.parse_args()
	
	if args.quiet:
		quietParameter["Allow"] = True

	if args.menu:
		try:
			menu()
			sys.exit()
		except KeyboardInterrupt:
			pass


	if args.min and args.max:
		if args.min > args.max:
			print(f"\n {backRed}{white}[!]{red}{backBlack} სავარაუდო ტექსტის {yellow}მინიმალური სიგრძე {red}ვერ იქნება {yellow}მაქსიმალურ სიგრძეზე {red}დიდი{endStyle}")
			sys.exit()


	if args.wordlist and args.type and args.string:
		try:
			dictionary(args.wordlist, args.type, args.string)
			sys.exit()
		except UnicodeDecodeError:
			print(f"\n\n {backRed}{white}[!]{red}{backBlack} ვეღარ ვაგრძელებ {yellow}ვორდლისტის {red}წაკითხვას, ვორდლისტი {yellow}დაზიანებულია{endStyle}")
			sys.exit()

	if args.type and args.string and args.min and args.max and args.list:
		try:
			if args.online:
				decrypt(args.type, args.string, args.min, args.max, args.list, args.online)
				sys.exit()
			else:
				decrypt(args.type, args.string, args.min, args.max, args.list)
				sys.exit()
		except KeyboardInterrupt:
			print(f'\n\n {backRed}{white}[!]{endStyle}{red}{backBlack} დეკრიპტაცია ძალით შეჩერდა{endStyle}')
			sys.exit()


	if args.keyword:
		customList.append(args.keyword)
		print(f"\n{backBlack} {white}[{green}INFO{white}] მოხდა შენი ქივორდების ინიციალიზაცია{endStyle}")

	if args.type and args.string and args.min and args.max and args.keyword: # ai aq
		try:
			if args.online:
				decrypt(args.type, args.string, args.min, args.max, 0, args.online)
				sys.exit()
			else:
				decrypt(args.type, args.string, args.min, args.max, 0)
				sys.exit()
		except KeyboardInterrupt:
			print(f'\n\n {backRed}{white}[!]{endStyle}{red}{backBlack} დეკრიპტაცია ძალით შეჩერდა{endStyle}')
			sys.exit()


	if args.type and args.string and args.online:
		try:
			onlineDatabase(args.string, args.type)
			sys.exit()
		except KeyboardInterrupt:
			print(f" {backRed}{white}[!]{endStyle}{red}{backBlack} ონლაინ ბაზებში შემოწმება ძალით გაჩერდა{endStyle}")
			sys.exit()

	if not args.list:
		crypt(args.string, args.type)
		sys.exit()

	if len(sys.argv) < 2:
		parser.print_usage()
		sys.exit()
