import serial, sys, os
import gtk, gobject

ser = serial.Serial("/dev/ttyACM0", 9600)

#window = gtk.Window()
#window.connect("destroy", gtk.main_quit)

#image = gtk.Image()
#window.add(image)
#image.set_from_file(os.path.join("/home/kblawlor/code/bronx/duino/image-arduino-project",'M39atlas.jpg'))

#window.show_all()
#gtk.main()

def pollSerial():
  sys.stdout.write(ser.read(1))
  sys.stdout.flush()
  return True

if (ser):
  print "Serial port: %s\n" % ser.portstr
  gobject.timeout_add(100, pollSerial)

gtk.main()
