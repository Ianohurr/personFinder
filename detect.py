import requests
import json



"""
Load an image from the web to be analyzed
Params: URL of the image
Returns: JSON file with the image analysis
"""
def loadImage(img_url):
    # put your keys in the header
    headers = {
        "app_id": "28cffa81",
        "app_key": "a53c47109871936d7d22221e9099ddb0"
    }
    payload = '{"image":"'+img_url+'"}'
    url = "http://api.kairos.com/detect"

    # make request
    r = requests.post(url, data=payload, headers=headers)
    r = r.json()
    return r

def getLikelyAge(attributes):
    return attributes['age']

def getLikelyGender(attributes):
    return attributes['gender']['type']

def getLikelyEthnicity(attributes):
    highest=0
    for item in attributes:
        if(item=='asian' or item=='black' or item=='hispanic' or item =='other' or item=='white'):
            if(attributes[item]>highest):
                highest=attributes[item]
                ethnicity=item
    return ethnicity

def printAttributes(imageStats):
    faces=imageStats['images'][0]['faces']
    print("Number of people detected in this photo: "+ str(len(faces))+'\n')
    for x in range(len(faces)):
        attributes=faces[x]['attributes']
        print("Attributes of the "+ str(x+1)+"st person: " + str(attributes))
        print("Detected age is: " +str(getLikelyAge(attributes)))
        print("Detected ethnicity is: " + getLikelyEthnicity(attributes))
        print("Detected gender is: " + getLikelyGender(attributes) +'\n')


def main():
    gem_ian="https://scontent.fphx1-2.fna.fbcdn.net/v/t1.0-9/1917425_104697396210017_762658_n.jpg?oh=3ea76844ec41f67c66de52766f28cb8d&oe=5B4C9287"
    alisa_ian="https://scontent.fphx1-2.fna.fbcdn.net/v/t31.0-8/22550416_1811880368825036_17198530836181250_o.jpg?oh=9f4d8d27e71a8f0787637be9292938ba&oe=5B0DE35F"
    five="https://scontent.fphx1-2.fna.fbcdn.net/v/t1.0-9/10392043_105686352777788_6746911_n.jpg?oh=144ba4398158ddddb8ce3f2c3d8ccbd2&oe=5B10CFE2"
    me_16="https://scontent.fphx1-2.fna.fbcdn.net/v/t1.0-9/155005_181805085165914_6636747_n.jpg?oh=f90e3a521f9daeb5827ff87f71746f45&oe=5B14340F"
    imageStats=loadImage(five)
    printAttributes(imageStats)

if __name__ == "__main__":
    main()