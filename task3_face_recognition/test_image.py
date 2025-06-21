import face_recognition
import cv2
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
known_face_names = ['biden','obama']

biden_encoding = face_recognition.face_encodings(biden_image)[0]
obama_encoding = face_recognition.face_encodings(obama_image)[0]

test_image = face_recognition.load_image_file("two_people.jpg")
face_locations = face_recognition.face_locations(test_image)
print('face_locations', face_locations)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

face_names = []
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces([biden_encoding,obama_encoding], face_encoding)
    name = "Unknown"
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    face_names.append(name)
print('detect faces', face_names)

# Display the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
    cv2.rectangle(test_image, (left, top), (right, bottom), (0, 0, 255), 2)
    # Draw a label with a name below the face
    cv2.rectangle(test_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(test_image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

test_image = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('output.jpg', test_image)