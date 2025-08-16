#List 

s3_bucket_list = ["abc_s3_bucket", "xyz_s3_bucket", "123_s3_bucket", "sdf_s3_bucket"]

print(s3_bucket_list)
print(len(s3_bucket_list))

s3_bucket_list.append("789_s3_bucket")

print(s3_bucket_list)
print(len(s3_bucket_list))

s3_bucket_list.remove("abc_s3_bucket")

print(s3_bucket_list)
print(len(s3_bucket_list))

print((s3_bucket_list) [0])

print((s3_bucket_list) [0:3])

number = [7, 9, 5, 1, 3]
number.sort()
print(number)


#Tuple

admin = ("Suhas", "admin")
print(admin)

# Cannot append or remove from tuple
# admin.append("admin2")     
