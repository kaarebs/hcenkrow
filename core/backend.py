import config.settings as settings
import MySQLdb as mdb
import sys

class Backend:
  def __init__(self):
    try:
      self.con = mdb.connect(settings.IP, settings.USER, settings.PASS, settings.DATABASE)
    except mdb.Error, e:
      print "Error %d: %s" % (e.args[0],e.args[1])
      sys.exit(1)

  def list(self,executionString):
    try:
      cur = self.con.cursor()
      cur.execute(executionString)
      return cur.fetchall()
    except mdb.Error, e:
      print "Error %d: %s" % (e.args[0],e.args[1])
      sys.exit(1)
    finally:    
      if self.con:    
        self.con.close()
