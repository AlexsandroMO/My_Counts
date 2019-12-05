from django.db import models


class TypeTask(models.Model):
    name_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name_type


class Task(models.Model):

    STATUS = (
        ('Pago', 'Pago'),
        ('Pagar', 'Pagar'),
    )
    type_task = models.ForeignKey(TypeTask, verbose_name='Tipo de Conta', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nome de Conta', max_length=255)
    description = models.TextField(verbose_name='Descrição de Conta', null=False)
    varcont = models.DecimalField(verbose_name='Valor da Conta', max_digits=5, decimal_places=2)
    done = models.CharField(verbose_name='Status da Conta', max_length=7,choices=STATUS,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name