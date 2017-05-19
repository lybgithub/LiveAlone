from Tkinter import *
import tkFileDialog as tkfile
from PIL import Image, ImageTk
import glob
import os
import tkMessageBox
import xml.etree.ElementTree as ET
from xml.dom import minidom


class Annotation():
    def __init__(self, master):
        # set up the main frame
        self.parent = master
        self.parent.title("Annotation Tool")
        self.frame = Frame(self.parent)
        self.frame.pack(fill = BOTH, expand = 1)
        self.parent.resizable(width = FALSE, height = FALSE)

        # initialize the mouse state
        self.state = {}
        self.state['click'] = 0;
        self.state['x'], self.state['y'] = 0, 0

        # initialize the image info
        self.imagedir = ''      # image directory
        self.img_index = 0      # image index
        self.total_img = 0      # image count
        self.cur_img = None     # open current image with PhotoImage
        self.imgname = ''       # image name
        self.imageset = []      # image name set
        self.name = ''          # uniform name for image and xml
        self.xml_path = ''      # xml file path

        # initialize the bbox container
        self.bboxlist = []  # save as (x1, y1, x2, y2, category)
        self.bboxset = []   # save the rectangles
        self.bbox = None    # draw the rectangles
        # reference of bbox
        self.ver_line = None
        self.hor_line = None


        # ----------GUI structure----------
        # load images and display the path
        self.label = Label(self.frame, text = "Image path:")
        self.label.grid(row = 0, column = 0, sticky = E, padx = 20)
        self.entry = Listbox(self.frame, height = 1)
        self.entry.grid(row = 0, column = 1, sticky = W+E)
        self.loadButton = Button(self.frame, text = "Load Image", width = 10, command = self.LoadImageDir)
        self.loadButton.grid(row = 0, column = 2, sticky = W+E, padx = 20, pady = 5)

        # set xml path
        self.xml = Label(self.frame, text = "Annotation path:")
        self.xml.grid(row = 1, column = 0, sticky = W, padx = 20)
        self.entry_xml = Listbox(self.frame, height = 1)
        self.entry_xml.grid(row = 1, column = 1, sticky = W+E)
        self.set_xml_Btn = Button(self.frame, text = "Set Xml Path", width = 10, command = self.setXmlPath)
        self.set_xml_Btn.grid(row = 1, column = 2, sticky = W+E, padx = 20, pady = 5)

        # canvas for adding labels
        self.canvas = Canvas(self.frame, cursor = "tcross", width = 500, height = 400)
        self.canvas.grid(row = 2, column = 1, rowspan = 5)
        self.canvas.create_rectangle(0, 0, 510, 410, fill = "gray")
        self.canvas.bind("<Button-1>", self.mouseClick)
        self.canvas.bind("<Motion>", self.mouseMove)
        self.parent.bind("<Escape>", self.cancelBBox)

        # bounding box info and label info
        self.bboxlabel = Label(self.frame, text = "category")
        self.bboxlabel.grid(row = 2, column = 2, sticky = E)
        self.entrylabel = Entry(self.frame, width = 15)
        self.entrylabel.grid(row = 2,column = 3, sticky = W, padx = 10)
        self.bboxtitle = Label(self.frame, text = "bbox info: (xmin, ymin, xmax, ymax, label)")
        self.bboxtitle.grid(row = 3, column = 2, columnspan = 2, sticky = N+S)
        self.bboxinfo = Listbox(self.frame, width = 30, height = 15)
        self.bboxinfo.grid(row = 4, column = 2, columnspan = 2, sticky = W+E, padx = 20)

        # bounding box operations
        self.addButton = Button(self.frame, text = "Delete", command = self.deleteBBox)
        self.addButton.grid(row = 5, column = 2, sticky = W+E, padx = 10, pady = 5)
        self.deleteButton = Button(self.frame, text = "Clear All", command = self.clearBBox)
        self.deleteButton.grid(row = 5, column = 3, sticky = W+E, padx = 15, pady = 5)

        self.saveButton = Button(self.frame, text = "Save xml_File", command = self.saveXmlFile)
        self.saveButton.grid(row = 6, column = 2, sticky = W+E, padx = 10, pady = 5)
        self.clearButton = Button(self.frame, text = "Exit", command = self.frame.quit)
        self.clearButton.grid(row = 6, column = 3, sticky = W+E, padx = 15, pady = 5)

        self.img_name = Label(self.frame, text = "")
        self.img_name.grid(row = 7, column = 0, padx = 10, sticky = W+E)

        self.pre_image = Button(self.frame, text = "Previous Image", width = 15, command = self.prevImage)
        self.pre_image.grid(row = 5, column = 0, padx = 5, pady = 10)
        self.next_image = Button(self.frame, text = "Next Image", width = 15, command = self.nextImage)
        self.next_image.grid(row = 6, column = 0, padx = 5, pady = 10)

        # A new frame to control image and display coords
        self.ctrlFrame = Frame(self.frame, border = 10)
        self.ctrlFrame.grid(row = 7, column = 1, columnspan = 4, sticky = W+E)

        self.img_number = Label(self.ctrlFrame, text = "%d / %d" % (self.img_index, self.total_img))
        self.img_number.grid(row = 0, column = 0, padx = 5, sticky = E)
        self.img_goto = Label(self.ctrlFrame, text = "Go to ")
        self.img_goto.grid(row = 0, column = 1, padx = 5, sticky = E)
        self.img_entry = Entry(self.ctrlFrame, text = "", width = 5)
        self.img_entry.grid(row = 0, column = 2, sticky = W)
        self.goBtn = Button(self.ctrlFrame, text = "Go", command = self.goToImage)
        self.goBtn.grid(row = 0, column = 3, sticky = E, padx = 5)

        self.mouse_position = Label(self.frame, text = "x = 0, y = 0")
        self.mouse_position.grid(row = 7, column = 2, padx = 5, sticky = W)
        self.saveinfo = Label(self.frame, text = "")
        self.saveinfo.grid(row =7, column = 3, padx = 5, sticky = E)

        # keyboard to control label work
        self.parent.bind("<Up>", self.prevImage)   # press 'Up' to previous image
        self.parent.bind("<Down>", self.nextImage)  # press 'Down' to previous image
        self.parent.bind("<Left>", self.prevImage)  # press 'Left' to previous image
        self.parent.bind("<Right>", self.nextImage)  # press 'Right' to previous image


    def LoadImageDir(self):
        self.imagedir = tkfile.askdirectory()      # open the image dir
        self.entry.insert(0, self.imagedir)
        self.imageset = glob.glob(os.path.join(self.imagedir, '*.jpg'))   # remember to change the image extension
        self.total_img = len(self.imageset)
        if(self.total_img == 0):
            tkMessageBox.showinfo("Warning", "No jpg image in this directory. Please check the image extension.")
            return
        self.img_index = 0
        self.LoadImage()


    def LoadImage(self):
        imagepath = self.imageset[self.img_index]
        self.imgname = os.path.split(imagepath)[-1]

        # print self.imgname
        self.img_name.config(text = self.imgname)
        self.img_number.config(text="%d / %d" % (self.img_index + 1, self.total_img))
        self.name = self.imgname.strip('.jpg')    # remember to change the extension

        self.clearBBox()
        self.saveinfo.config(text = "")

        pro_image = Image.open(imagepath)
        self.cur_img = ImageTk.PhotoImage(pro_image)
        self.width = int(self.cur_img.width())
        self.height = int(self.cur_img.height())
        self.ratio = 1

        if self.width > 500 or self.height > 400:
            w_ratio = self.width/500.
            h_ratio = self.height/400.
            self.ratio = w_ratio
            if h_ratio > w_ratio:
                self.ratio = h_ratio

        # resize the image and no change for image ratio
        self.new_image = pro_image.resize((int(self.width/self.ratio), int(self.height/self.ratio)), Image.BILINEAR)
        self.cur_img = ImageTk.PhotoImage(self.new_image)

        self.canvas.create_image(0, 0, image = self.cur_img, anchor = NW)
        if self.xml_path == '':
            tkMessageBox.showinfo("Warning", "Please set the xml path !")
        self.LoadAnnotation()

    def setXmlPath(self):
        self.xml_path = tkfile.askdirectory()
        self.entry_xml.insert(0, self.xml_path)
        self.LoadAnnotation()

    def LoadAnnotation(self):
        xml_name = os.path.join(self.xml_path, self.name + '.xml')
        if os.path.exists(xml_name):
            tree = ET.parse(xml_name)
            objs = tree.findall('object')
            for id, obj in enumerate(objs):
                name = obj.find('name')
                category = name.text
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)
                # insert to bboxlist
                self.bboxlist.append((xmin, ymin, xmax, ymax, category))
                self.bboxinfo.insert(END, '(%d, %d, %d, %d, %s)' % (xmin, ymin, xmax, ymax, category))
                # insert to bboxset and draw the rectangle
                self.bbox = self.canvas.create_rectangle(int(xmin/self.ratio), int(ymin/self.ratio),
                                                         int(xmax/self.ratio), int(ymax/self.ratio),
                                                         outline = "#7CFC00", width = 2)
                self.bboxset.append(self.bbox)
                self.bbox = None


    def mouseClick(self, event):
        if self.state['click'] == 0:
            self.state['x'], self.state['y'] = event.x, event.y

        else:
            # get x1, y1, x2, y2 of bbox
            x1, x2 = min(self.state['x'], event.x), max(self.state['x'], event.x)
            y1, y2 = min(self.state['y'], event.y), max(self.state['y'], event.y)

            # transform to origianl size and process the boundary
            x1 = max(int(x1 * self.ratio), 0)
            y1 = max(int(y1 * self.ratio), 0)
            x2 = min(int(x2 * self.ratio), self.width)
            y2 = min(int(y2 * self.ratio), self.height)

            # get the category from enrty
            category = self.entrylabel.get()
            if category == "":
                tkMessageBox.showinfo("Warning", "Please input the category !")
                return

            self.bboxset.append(self.bbox)
            self.bbox = None
            self.bboxlist.append((x1, y1, x2, y2, category))
            self.bboxinfo.insert(END, '(%d, %d, %d, %d, %s)' % (x1, y1, x2, y2, category))

        self.state['click'] = 1 - self.state['click']

    def mouseMove(self, event):
        self.mouse_position.config(text = "x = %d, y = %d" % (event.x, event.y))
        # draw the reference line
        if self.cur_img:
            if self.hor_line:
                self.canvas.delete(self.hor_line)
            self.hor_line = self.canvas.create_line(0, event.y, self.cur_img.width(), event.y, fill = "#97FFFF")
            if self.ver_line:
                self.canvas.delete(self.ver_line)
            self.ver_line = self.canvas.create_line(event.x, 0, event.x, self.cur_img.height(), fill = "#97FFFF")
        # draw the current bbox
        if self.cur_img:
            if self.state['click'] == 1:
                if self.bbox:
                    self.canvas.delete(self.bbox)
                self.bbox = self.canvas.create_rectangle(self.state['x'], self.state['y'], event.x, event.y, outline = "#7CFC00", width = 2)

    def cancelBBox(self, event):
        if self.state['click'] == 1:
            if self.bbox:
                self.canvas.delete(self.bbox)
                self.bbox = None
                self.state['click'] = 0


    def prevImage(self, event = None):
        if self.cur_img != None:
            self.saveXmlFile()
            if self.img_index <= 0:
                tkMessageBox.showinfo("Warning", "This is the first image.")
                return
            self.img_index -= 1
            self.LoadImage()

    def nextImage(self, event = None):
        if self.cur_img != None:
            self.saveXmlFile()
            if self.img_index >= self.total_img - 1:
                tkMessageBox.showinfo("Warning", "This is the last image.")
                return
            self.img_index += 1
            self.LoadImage()

    def goToImage(self):
        if self.cur_img != None:
            self.saveXmlFile()
            if self.img_entry.get() != "":
                number = int(self.img_entry.get())
                if number >=1 and number <= self.total_img:
                    self.img_index = number - 1
                    self.LoadImage()
                else:
                    tkMessageBox.showinfo("Warning", "Invalid input number !")

    def deleteBBox(self):
        # get current selection
        cur_bbox = self.bboxinfo.curselection()
        # delete only one bbox
        if len(cur_bbox) != 1:
            return;
        bbox_ind = int(cur_bbox[0])

        self.canvas.delete(self.bboxset[bbox_ind])  # delete rectangle
        self.bboxlist.pop(bbox_ind)                 # delete from bboxlist info
        self.bboxset.pop(bbox_ind)                      # delete from rectangle set
        self.bboxinfo.delete(bbox_ind)              # delete from bboxlist display

    def clearBBox(self):
        bbox_len = len(self.bboxlist)
        if bbox_len == 0:
            return
        for id in range(bbox_len):
            self.canvas.delete(self.bboxset[id])
        self.bboxinfo.delete(0, bbox_len)
        self.bboxlist = []
        self.bboxset = []

    def saveXmlFile(self):
        if self.xml_path == '':
            tkMessageBox.showinfo("Warning", "Please set the xml path first !")
            return

        xml_name = os.path.join(self.xml_path, self.name + '.xml')
        # print xml_name
        root = ET.Element('annotation')
        for element in self.bboxlist:
            object = ET.SubElement(root, 'object')
            name = ET.SubElement(object, 'name')
            bbox = ET.SubElement(object, 'bndbox')
            name.text = element[-1]

            xmin = ET.SubElement(bbox, 'xmin')
            ymin = ET.SubElement(bbox, 'ymin')
            xmax = ET.SubElement(bbox, 'xmax')
            ymax = ET.SubElement(bbox, 'ymax')
            xmin.text = str(element[0])
            ymin.text = str(element[1])
            xmax.text = str(element[2])
            ymax.text = str(element[3])

        rough_string = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        result = reparsed.toprettyxml(indent="  ")

        file = open(xml_name, 'w')
        file.write(result)

        self.saveinfo.config(text = "saved successfully !")



if __name__ == "__main__":
    root = Tk()
    tool = Annotation(root)
    root.mainloop()