from django.db import models

class Kurs(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField
    davomiylik = models.CharField(max_length=30)
    dars_narxi = models.PositiveSmallIntegerField()

class Ustoz(models.Model):
    ism_fam = models.CharField(max_length=60)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    daraja = models.CharField(max_length=30)
    tel = models.IntegerField()

class Xona(models.Model):
    qavat = models.IntegerField()
    xona = models.IntegerField()
    nom = models.CharField(max_length=50, null=True, blank=True)
    sigim = models.PositiveSmallIntegerField()

class Oquvchi(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    qayerdan = models.CharField(max_length=50)
    tel = models.PositiveSmallIntegerField()
    tel2 = models.PositiveSmallIntegerField()



class Guruh(models.Model):
    nom = models.CharField(max_length=30)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    kun = models.CharField(max_length=50, choices=(
        ("Du-Chorshanba-Juma","Du-Chorshanba-Juma"),
        ("Se-Payshanba-Shanba","Se-Payshanba-Shanba")
    ))
    vaqt = models.PositiveSmallIntegerField()
    oquvchilar = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)


class Tolov(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    chegirma = models.PositiveSmallIntegerField ()
    summa = models.IntegerField()
    oy = models.CharField(max_length=30)
    yil = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)
    admin = models.CharField(max_length=50)
    turi = models.CharField(max_length=50)

class Davomat(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    holat = models.CharField(max_length=30, choices=(
        ("Keldi","Keldi"),
        ("Kelmadi","Kelmadi")
    ))
    sana = models.DateField()

# Create your models here.
