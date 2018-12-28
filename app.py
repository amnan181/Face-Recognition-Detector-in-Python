# English:
#   import the libraries
# Urdu:
#   libraries sb sy pahly import krain 
import os
import face_recognition

# English:
#   make a list of all the available images.This instruction maka a list ex.['1.jpg','2.jpg','3.jpg','4.jpg']
# Urdu:
#   y instruction ya line aik makhsoos folder sy tamam image fetch krti h.or un image ky naam ko aik list mn return krti h ex.['1.jpg','2.jpg','3.jpg','4.jpg']
images = os.listdir('images')

# English:
#   load your image which you are recognition
# Urdu:
#   es line mn wo image dyn jis ko ap recognize kerna chahty hn
image_to_be_matched = face_recognition.load_image_file('unknown.jpg')


# English:
#   encoded the loaded image into a feature vector
# Urdu:
#   jo image ap ny recognition ky liy li h y line us ko encode krti h taky usy baad mn compare kia jay dosri images ky sath
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]


# English:
#   iterate over each image
# Urdu:
#   Es process mn hm folder mn tamam picure ky sath apni makhsoos krda picture ko recognize krain gay
for image in images:
    # English:
    #   load the image
    # Urdu:
    #   y hamary folder sy tamam image bari bari load kry ga
    current_image = face_recognition.load_image_file("images/" + image)
    # |----------------SAME----------------|
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # English:
    #   match your image with the image and check if it matches
    # Urdu:
    #   Y hamari makhsoos image ko hamry folder ki tamam image ky sath bari bari compare kry ga
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # English:
    #   check if it was a match
    # Urdu:
    #   yaha hm apna result check krain gay
    if result[0] == True:
        print("Matched: " + image)
    else:
        print("Not matched: " + image)
