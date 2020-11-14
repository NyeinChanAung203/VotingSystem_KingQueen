# import hashlib
# for i in range(2,11):
# 		user_code = 'VKQ1cs'+ str(i)
# 		hashobj =  hashlib.md5()
# 		hashobj.update(user_code.encode())
# 		md5_value = hashobj.hexdigest()
# 		vu = VotingUser.objects.create(name=f'1cs{i}',qr_code=md5_value)
# 		print(vu.name,vu.qr_code,vu.voting_attempt)
# 		vu.save()




#Generate QR code img
# import pyqrcode
# import time
# for i in range(2,11):
# 	user_code = 'VKQ1cs'+ str(i)
# 	hashobj =  hashlib.md5()
# 	hashobj.update(user_code.encode())
# 	md5_value = hashobj.hexdigest()
# 	qr = pyqrcode.create(md5_value)
# 	qr.png(f'/root/Pictures/qr_code/1cs{i}.png',scale=10)
# 	print(user_code,':',md5_value,len(hashobj.hexdigest())) 
# 	time.sleep(1)