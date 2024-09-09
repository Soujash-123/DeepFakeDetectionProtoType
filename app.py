import os
os.system("pip install -r requirements.txt")
os.popen("python 00-convert_video_to_image.py")
os.popen("python 01a-crop_faces_with_mtcnn.py")
os.popen("python 01b-crop_faces_with_azure-vision-api.py")
os.popen("python 02-prepare_fake_real_dataset.py")
os.popen("python 03-train_cnn.py")
