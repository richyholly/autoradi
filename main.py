datei = open('TEST-EUT.EUT', 'w', encoding="utf-16")   #Datei mit Dateinamen 'TEST-EUT' erstellen, mit a werden geschriebene Zeilen angefügt
datei.writelines(['"Device Data File"','\r"Device Data for Test SerialNr.:"'])
for i in range (0, 2):
    datei.write('\r""')
datei.write('\r11')
for i in range (0, 11):
    datei.write('\r""')
datei.write('\r11')
for i in range (0, 11):
    datei.write('\r""')
datei.writelines(['\r11','\r"Company"','\r"Name"','\r"Adress','\r"ZIP"', '\r"City"', '\r"0000-14151617"'])

datei.close()
            
