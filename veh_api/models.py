from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=30)
    vehicle_processed = models.IntegerField()
    wanted_matches_identified = models.IntegerField(null=True)
    ticketed_matches_identified = models.IntegerField(null=True)
    percentage_ticketed_matches = models.IntegerField(null=True)
    percentage_operations_processed = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']


class SubOrganisation(models.Model):
    org_name = models.ForeignKey(Organisation,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=30)
    vehicle_processed = models.IntegerField()
    wanted_matches_identified = models.IntegerField(null=True)
    ticketed_matches_identified = models.IntegerField(null=True)
    percentage_ticketed_matches = models.IntegerField(null=True)
    percentage_operations_processed = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.org_name} {self.sub_name}'


class SubOrganisationData(models.Model):
    sub_org_name = models.ForeignKey(SubOrganisation,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=30)
    vehicle_processed = models.IntegerField()
    wanted_matches_identified = models.IntegerField(null=True)
    ticketed_matches_identified = models.IntegerField(null=True)
    percentage_ticketed_matches = models.IntegerField(null=True)
    percentage_operations_processed = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.sub_org_name} {self.sub_name}'