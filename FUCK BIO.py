import requests as re
se = re.Session()
h = {
'X-BBCOLLAB-AUTH-TOKEN': 'e4071403-6a56-45cb-ba3c-24baa8ff6bae',
'Referer': 'https://eu.bbcollab.com/collab/ui/session/join/9be3c79d237742c09925bd7cfad8f4e7',

'Cookie': 'BbCollabClientUUID=96f5a32a-34b8-4fb0-a420-577fdf34cf03; zjsdk.username.saturn=43'
}
# g = se.get("https://eu.bbcollab.com/collab/ui/session/guest/daadf0d3b1ae4530bbd42502b0e7f572",headers = h)
# k = se.post("https://eu.bbcollab.com/collab/ui/session/guest/daadf0d3b1ae4530bbd42502b0e7f572",headers = h)
g = se.get("https://eu.bbcollab.com/collab/ui/session/guest/daadf0d3b1ae4530bbd42502b0e7f572", headers=h, stream=True)
print(g)
for i in g.iter_lines():
    if i:
        print(i)











