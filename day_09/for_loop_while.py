#for i in range(10):
    #print(i)

s3_list = [1, "a", 4, 7, "b"]

#for i in s3_list:
    #print(i)

for i in s3_list:
    if i == 4:
        break
    print(i)

for i in s3_list:
    if i == 4:
       continue
    print(i)


#bash script
  # while kubectl get deployment/myapp | grep -q 0/1; do
    #   echo "Waiting for myapp to be ready..."
    #   sleep 10
  # done
#