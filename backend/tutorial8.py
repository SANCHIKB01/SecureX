# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# # Initialize warning count
# warning_count = 0
# previous_warning_state = False

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     # Count of detected faces
#     face_count = len(faces)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 5)  # Yellow box for face
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)  # Green box for eyes

#     # Display warning message if multiple faces are detected
#     if face_count > 1:
#         if not previous_warning_state:  # Only increase count once for consecutive frames
#             warning_count += 1
#         previous_warning_state = True
#     else:
#         previous_warning_state = False  # Reset warning state if no multiple faces

#     if warning_count > 0:
#         warning_text = f"Warning: Multiple faces detected! Warning Count: {warning_count}"
#         cv2.putText(frame, warning_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
