# Rollcall
An automatic attendance management system that can take attendance of the students in a class and create excel sheet to store the attendance.
This is a device which is created using raspberry pi and camera v2


## Device

![IMG-20191111-WA0016](https://user-images.githubusercontent.com/18730159/88021964-08929a80-cb4c-11ea-8c6f-3e73dcdc2ecc.jpg)

## Tech Stack

* Opencv2
* Microsoft Cognitive Services
* dlib
* SQLite
* openpxyl
* Uses Micosoft Cognitive Face API to recognizes faces in picture from cctv or clicked from mobile devices (source can varry) and marks the attendace of each     student present in picture

| FILE	             |  DESC                                                                            |
---------------------|-------------------------------------------------------------------------------------
|Face-DataBase	     |   Database                                                                         |
|dataset	           |   (A dataset) contains dir with faces of each student                              |
|add_student.py	     |   make dataset and entry in DB                                                     |
|create_person.py	   |   generate personId from microsoft server                                          |
|add_person_faces.py |	 generate faceIds for each face in dataset                                       |
|train.py	           |   trains the model in microsoft server                                             |
|get_status.py	     |   show the current status                                                          |
|spreadsheet.py	     |   makes xls sheet named reports.xlsx                                                |
|detect.py	         |   detect faces in test picture and crops and put them in Cropped_faces directory   |
|identify.py	       |   identify each face and marks the attendance                                      |
|layout.py           |   A gui to get details of the student and photos to train the model                |


