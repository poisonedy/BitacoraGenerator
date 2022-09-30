import os
from pathlib import Path
import datetime


class timeline:

    def __init__(self, directory):

        self.directory = directory

        self.timelinesPath = os.path.join(os.getcwd(), 'bitacoras')
        self.mainTimeline = os.path.join(self.timelinesPath, self.directory)
        self.timelineSlots = []
        self.loadSlots()
        self.sortSlots()
        self.allHtml = ''
        print (self.generateHtml())


    def generateHtml (self):
        self.allHtml = '''<!DOCTYPE html>
                            <html>
                            <head>
                            '''
        self.allHtml = self.allHtml + "<title>" + os.path.basename(self.mainTimeline) + "</title>"
        self.allHtml = self.allHtml + '''
                            <style>
                            body {
                                font-family: Arial, Helvetica, sans-serif;
                            background-color: Moccasin;
                            text-align: left;
                            color: DarkSlategray;
                                    }
                            </style>
                            </head>
                            <body>
                            
                            '''

        for slot in self.timelineSlots:
            self.allHtml = self.allHtml + '''                    <table style="border-collapse: collapse; width: 100%; background-color: RosyBrown" border="0">
                    <tbody>
                    <tr>
                    <td style="width: 100%;">'''

            self.allHtml = self.allHtml + "<h1>" + slot.dateSlot.strftime("%d %b %Y") + "</h1>\n"
            self.allHtml = self.allHtml + '''
                            &nbsp;</td>
                                    </tr>
                                    </tbody>
                                    </table>
            '''

            for items in slot.slotItems:

                self.allHtml = self.allHtml + '''                    <table style="border-collapse: collapse; width: 100%;background-color: SandyBrown" border="0">
                                                 <tbody>
                                                    <tr>
                                                    <td style="width: 100%;">'''
                self.allHtml = self.allHtml + "<h2>" + str(items.timeslot) + "</h2>\n"
                self.allHtml = self.allHtml + '''
                            &nbsp;</td>
                                    </tr>
                                    </tbody>
                                    </table>
            '''
                for item in items.hourSlotFiles.items():
                    
                    self.allHtml = self.allHtml + '''
                    <table style="border-collapse: collapse; width: 100%; height: 25px;border-color: SandyBrown" border="">
                    <tbody>
                    <tr style="height: 25px;">
                    <td style="width: 50%; height: 25px;background-color: LightGray">
                    <table style="border-collapse: collapse; width: 100%; height: 36px;" border="0">
                    <tbody>
                    <tr style="height: 18px;">
                    <td style="width: 100%; height: 18px;background-color: Silver">
                    '''

                    self.allHtml = self.allHtml + "<h3>" + item[0] + '</h3>\n</td>\n</tr><tr style="height: 18px;">'
                    self.allHtml  = self.allHtml + '<td style="width: 100%; height: 18px;background-color: White"><p>' + item[1] + "<p>\n</td>\n"
                    self.allHtml = self.allHtml + '''</tr>
                                                        </tbody>
                                                        </table>
                                                        </td>
                                                    <td style="width: 50%; height: 25px;background-color: LightGray">
                                                     
                                                    '''
                    self.allHtml = self.allHtml + self.generateMediaWidget(self.directory,slot.slotpathBasename,str(items.basename),item[0])

            self.allHtml = self.allHtml + '''
            
            <table style="border-collapse: collapse; width: 1.8466%; height: 226px;background-color: SandyBrown" border="0">
                        <tbody>
                        <tr style="height: 226px;">
                <td style="width: 100%; height: 226px;"></td>
                        </tr>
                        </tbody>
                    </table>
            
            '''



        self.allHtml = self.allHtml + '''
                <h1>Final de Documento</h1>
                </body>
                </html>

                        '''

        with open( self.directory + ".html", 'w') as htmlpage:
            htmlpage.write(self.allHtml)

        return self.allHtml


        '''
        for slot in tl.timelineSlots:
            print ("Date: " + str(slot.dateSlot.strftime("%d %b %Y")))
            for items in slot.slotItems:
                print (items.timeslot)
                #print (items.hourSlotFiles)
                for item in items.hourSlotFiles.items():
                    print (item[0],item[1])
        '''

    def generateMediaWidget (self, directory, slotbasename, itemsbasename, itemfile):

        if "mp3" in itemfile:

            htmlCode = "<audio controls>\n" + '<source src="bitacoras/' + directory + "/" + slotbasename + "/" + itemsbasename + "/" + itemfile.strip() +'''
                                                    " type="audio/mp3">
                                                    Your browser does not support the audio element.
                                                    </audio> 
                                                    </tr>
                                                    </tbody>
                                                    </table>
                                                    '''
        
        elif "ogg" in itemfile:

            htmlCode = "<audio controls>\n" + '<source src="bitacoras/' + directory + "/" + slotbasename + "/" + itemsbasename + "/" + itemfile +'''
                                                    " type="audio/ogg">
                                                    Your browser does not support the audio element.
                                                    </audio> 
                                                    </tr>
                                                    </tbody>
                                                    </table>
                                                    '''
        
        elif "mp4" in itemfile:

            htmlCode = ' <video width="320" height="240" controls><source src="bitacoras/' + directory + "/" + slotbasename + "/" +itemsbasename + "/" +itemfile +'''
                                                    "type="video/mp4">
                                                    Your browser does not support the video element.
                                                    </video> 
                                                    </tr>
                                                    </tbody>
                                                    </table>
                                                    '''
        
        elif "jpeg" in itemfile or "jpg" in itemfile or "png" in itemfile:

            htmlCode = '<a href="'+ "bitacoras/" + directory + "/" + slotbasename + "/" +itemsbasename + "/" +itemfile + '"><img src="' + "bitacoras/" + directory + "/" + slotbasename + "/" +itemsbasename + "/" + itemfile +  '''
            
                                "width="20%"/></a>
                                 </tr>
                                                    </tbody>
                                                    </table>

                                '''

        elif "pdf" in itemfile:

            htmlCode = '<a href="'+ "bitacoras/" + directory + "/" + slotbasename + "/" +itemsbasename + "/" + itemfile + '"target=_blank">Ver Pdf</a>' + '''
            </tr>
            </tbody>
            </table>
            
            '''

        else:

            htmlCode = "SIN ARCHIVOS\n</tr>\n</tbody>\n</table>"

        return htmlCode

    
    def getTimelinePath (self):

        return self.mainTimeline


    def loadSlots(self):

        with os.scandir(self.mainTimeline) as entries:

            for entry in entries:

                self.timelineSlots.append(dateSlot(os.path.join(self.mainTimeline, entry.name)))           
         

    def getSlotItems(self, slot):

        for item in self.timelineSlots:

            if slot in item.slotPath:

                return item.slotItems


    def getSlotItemsData (self, slot):

        myItems = self.getSlotItems(slot)

        for item in myItems:

            item.getFilesFromDateSlot()


    def sortSlots(self):

        self.timelineSlots = sorted(self.timelineSlots, key=lambda x: x.dateSlot)


class dateSlot:
    
    def __init__(self, slotPath):

        self.slotPath = slotPath
        self.slotpathBasename = os.path.basename(self.slotPath)
        self.dateSlot = self.setDate()
        self.slotItems = []
        self.loadSlotItems()

    def path (self):

        return self.slotPath

    def setDate(self):

        dateTemp = os.path.basename(self.slotPath).split("-")
        return datetime.date(int(dateTemp[2]), int(dateTemp[1]), int(dateTemp[0]))

    def loadSlotItems (self):

        with os.scandir(self.slotPath) as entries:

            for entry in entries:

                self.slotItems.append(hourSlot(os.path.join(self.slotPath, entry.name)))

    
    def getSlotItems (self):

        return self.slotItems


class hourSlot:

    def __init__(self, filepath):

        self.filepath = filepath
        self.basename = os.path.basename(self.filepath)
        self.timeslot = ""
        self.setTimeSlot()
        self.hourSlotInfo = self.getDateSlotInfoTxt()
        self.filetype = os.path.basename(self.filepath).split(".", 1)
        self.itemsFiles = []
        self.hourSlotFiles = {}
        self.getFilesFromDateSlot()

    def setTimeSlot(self):

        self.timeslot = os.path.basename(self.filepath).split("_")
        self.timeslot = datetime.time(int(self.timeslot[0]), int(self.timeslot[1]))


    def getDateSlotInfoTxt(self):

        try:
            
            with open(os.path.join(self.filepath,'info.txt')) as info:

                lines = info.readlines()

            return lines
        
        except:

            raise Exception ("no info file in " + self.filepath)


    def getFilesFromDateSlot(self):

        count = 0

        for line in self.getDateSlotInfoTxt():

            try:

                if count % 2 == 0:

                    self.hourSlotFiles[line] = ''
                    lastLine = line
                    count = count + 1
                
                else:

                    self.hourSlotFiles[lastLine] = line
                    count = count + 1
        

            except ZeroDivisionError:

                self.hourSlotFiles[line] = ''
                lastLine = line
                count = count + 1

        #return self.myFileDict
            



tl = timeline ("eric")
'''
for slot in tl.timelineSlots:
    print ("Date: " + str(slot.dateSlot.strftime("%d %b %Y")))
    for items in slot.slotItems:
        print (items.timeslot)
        #print (items.hourSlotFiles)
        for item in items.hourSlotFiles.items():
            print (item[0],item[1])
'''
