from pine import upload_to_pinecone

with open("comprehensions.txt",'r') as f:
    raw_txt = f.read()

raw_txt_list = raw_txt.split("$$")

raw_txt_list = list(map(lambda x : x.strip(),raw_txt_list))


try :
    for txt_idx in range(len(raw_txt_list)):
        if len(raw_txt_list[txt_idx])>0:
            upload_to_pinecone(f"id_{txt_idx}","comprehension",raw_txt_list[txt_idx])
            print(f"Uploaded text : {txt_idx}")
        else :
            print("Empty item!")
    
    print("Uploaded all items!")
except:
    print("Error while uploading!\nExiting!")