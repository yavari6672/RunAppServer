from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=17)
    description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.name}({self.ip_address}):{self.description}'


class Service(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=27)
    port = models.IntegerField()
    description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.name}({self.port}):{self.description}'
