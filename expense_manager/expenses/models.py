from django.db import models

class Expense(models.Model):
    EXPENSE_TYPES = [
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('other', 'Other'),
    ]

    date = models.DateField()
    cost_gbp = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)

    def __str__(self):
        return f"{self.description} - £{self.cost_gbp}"