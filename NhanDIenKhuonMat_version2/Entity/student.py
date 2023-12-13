from NhanDIenKhuonMat_version2.extension import db

# class Students ------------------------------------------

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msv = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, nullable=False)

    def __call__(self):
        pass

    def __init__(self, msv, fullname):
        self.fullname = fullname
        self.msv = msv

    def __str__(self):
        return self.msv + " " + self.fullname

    def getMsv(self):
        return self.msv

    def getFullname(self):
        return self.fullname

    def getId(self):
        return self.id

    def getLastname(self):
        lastname = str(self.fullname).split()
        return lastname[len(lastname) - 1]
# class end -------------------------------------------------------
