# import cv2
# import numpy as np
# import pyautogui
# import time

# SCREEN_SIZE = (1920, 1080)

# # codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

# fps = 120
# prev = 0

# while True:
#     time_elapsed = time.time() - prev
#     img = pyautogui.screenshot()

#     if time_elapsed > 1.0 / fps:
#         prev = time.time()
#         frame = np.array(img)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output.write(frame)

#     cv2.waitKey(100)

# cv2.destroyAllWindows()
# output.release()


import numpy as np
import cv2
import pyscreenshot as pys

forcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("outpst.avi", forcc, 8, (1920, 1080))


while True:
    img = pys.grab()
    img_np = np.array(img)

    # frame= cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("Screen", img_np)
    out.write(img_np)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

out.release()
cv2.destroyAllWindows()
