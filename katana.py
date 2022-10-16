#!/usr/bin/python3
# Coded by - WebDux (vakh0) -

from termcolor import colored
from printy import printy
import hashlib, os, time, sys, itertools

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
purple = '\033[35m'
lightgrey = '\033[37m'
lightgreen = '\033[92m'
yellow = '\033[93m'

list1 = ' abcdefghijklmnopqrstuvwxyx'
list2 = ' abcdefghijklmnopqrstuvwxyx0123456789'
list3 = ' abcdefghijklmnopqrstuvwxyx[]{}"!@#$%^&*().,/;'
list4 = ' abcdefghijklmnopqrstuvwxyx0123456789[]{}"!@#$%^&*().,/;'
list5 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
list6 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ0123456789'
list7 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ[]{}"!@#$%^&*().,/;'
list8 = ' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ0123456789[]{}"!@#$%^&*().,/;'




def decrypt(hashMethod, string, maxLenght, listChoice):
	success = False
	datvla = 0
	maxLenght = maxLenght + 1
	match listChoice:
		case 1:
			usingList = list1
		case 2:
			usingList = list2
		case 3:
			usingList = list3
		case 4:
			usingList = list4
		case 5:
			usingList = list5
		case 6:
			usingList = list6
		case 7:
			usingList = list7
		case 8:
			usingList = list8
	
	startTime = time.time()
	sys.stdout.write(f"\n {yellow}[+]      პარამეტრები: | ტიპი: {purple}{hashMethod}{yellow} ლექსიკონი: {purple}{listChoice}{yellow} სიმბოლო: {purple}{maxLenght-1}\n")
	sys.stdout.flush()
	print(colored(f" {yellow}[+] დაშიფრული ტექსტი: |{blue} {string} {yellow}|","yellow"))
	startTime = time.time()
	for n in range(1, maxLenght):
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
			sys.stdout.write(f"\r {yellow}[+]     ვიყენებ ჰეშს: | {red}{shifri}{yellow} |")
			sys.stdout.flush()
			if string == shifri:
				sys.stdout.write(f"\r {yellow}[+]     ვიყენებ ჰეშს: | {blue}{shifri}{yellow} \n")
				print(f" [+]           შედეგი: | ცდა: {purple}{datvla}{yellow} - წამი: {purple}{timeNOW}")
				print(f" {green}[+]           ტექსტი: {yellow}| {lightgreen}{Generated} ")
				success = True
				break
	if not success:
		sys.stdout.write(f"\r {yellow}[-]     ვიყენებ ჰეშს: | {red}{shifri}{yellow} |")
		print(f"\n {red}[!]           ტექსტი: {yellow}|{lightgrey} \033[41mვერ გაიშიფრა\033[0;30m")


def menu():
	printy("\n --- Welcome to Katana --- ", "rBU")
	print(colored("\n[1] დაშიფვრა",'yellow'))
	print(colored("[2] გაშიფვრა",'yellow'))
	print(colored("[3] ანალიზი",'yellow'))
	choice = input(colored("\n[?]- ", "blue"))

	if choice == "1":
		print(colored("- მეთოდები -\nmd5, sha1, sha224, sha256, sha384, sha512", "red"))
		hashMethod = input(colored("[?] ჰეშირების მეთოდი: ", "yellow"))
		string = input(colored("[?] ტექსტი: ", "yellow"))
		crypt(string, hashMethod)
	elif choice == "2":

		print(colored("- მეთოდები -\nmd5, sha1, sha224, sha256, sha384, sha512", "red"))
		hashMethod = input(colored("[?] ჰეშირების მეთოდი: ", "yellow"))
		string = input(colored("[?] დაშიფრული ტექსტი: ", "yellow"))
		maxLenght = int(input(colored("[?] ტექსტის მაქსიმალური სიგრძე: ", "yellow")))
		print(colored(f"\n{red}-[ სიმბოლოების ნაკრები ]-\n{blue}1: {list1}\n2: {list2}\n3: {list3}\n4: {list4}\n5: {list5}\n6: {list6}\n7: {list7}\n8: {list8}\n"))
		selectedList = int(input(colored("[!]: აირჩიე სიმბოლოების ნაკრები: ", "yellow")))
		
		match hashMethod:
			case "md5":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case "sha1":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case "sha224":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case "sha256":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case "sha384":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case "sha512":
				decrypt(hashMethod, string, maxLenght, selectedList)
			case _:
				print("[!] მიუთითე ჩამოთვლილიდან რომელიმე")
	elif choice == "3":
		string = input(colored("[!] შეიყვანე დაშიფრული ტექსტი: ", "green"))
		os.system("hashid " + string)


def crypt(string, hashMethod):
	match hashMethod:
		case "md5":
			result_MD5 = hashlib.md5(string.encode())
			print("\nMD5: ", colored(result_MD5.hexdigest(),'blue'))
		case "sha1":
			result_SHA1 = hashlib.sha1(string.encode())
			print("\nsha1: ", colored(result_SHA1.hexdigest(),'blue'))
		case "sha224":
			result_SHA224 = hashlib.sha224(string.encode())
			print("\nsha224: ", colored(result_SHA224.hexdigest(),'blue'))
		case "sha256":
			result_SHA256 = hashlib.sha256(string.encode())
			print("\nsha256: ", colored(result_SHA256.hexdigest(),'blue'))
		case "sha384":
			result_SHA384 = hashlib.sha384(string.encode())
			print("\nsha384: ", colored(result_SHA384.hexdigest(),'blue'))
		case "sha512":
			result_SHA512 = hashlib.sha512(string.encode())
			print("\nsha512: ", colored(result_SHA512.hexdigest(),'blue'))
	

if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt:
		pass