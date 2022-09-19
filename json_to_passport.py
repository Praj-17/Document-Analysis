import json
import cv2


filename = 'result.json'
def save_cropped_images(json_file):
    json_data = json.load(open(json_file))
    json_data = json_data[0]
    objects = json_data['objects']
    
    image = cv2.imread('boss2.jpg')
    for id, object in enumerate(objects):
        x = object['relative_coordinates']['center_x']
        y = object['relative_coordinates']['center_y']
        w = object['relative_coordinates']['width']
        h = object['relative_coordinates']['height']
        x = int(x * image.shape[1])
        y = int(y * image.shape[0])
        w = int(w * image.shape[1])
        h = int(h * image.shape[0])
        x1,y1,x2,y2=x,y,x+w,y+h
        p1,p2 = (x1-int(w/1.2),y1-int(h/1.2)), (x2+int(w/5), y2+int(h/5)) 
        if p1[0]<0:
            p1 = (0,p1[1])
        if p1[1]<0:
            p1 = (p1[0],0)
        cropped_image = image[p1[1]:p2[1], p1[0]:p2[0]]
        cv2.imwrite(f'saved_{id}.jpg',cropped_image)
    print('images saved successfully')     
    
save_cropped_images(filename)  
