from django.test import TestCase
from .models import Expense
from datetime import date
from rest_framework.test import APIClient

class ExpenseModelTest(TestCase):
    def test_create_expense(self):
        expense = Expense.objects.create(
            date=date.today(),
            cost_gbp=100.50,
            description="Test expense",
            expense_type="food"
        )

        self.assertEqual(expense.description, "Test expense")
        self.assertEqual(expense.cost_gbp, 100.50)

class ExpenseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_expenses(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)

    def test_create_expense(self):
        data = {
            "date": "2026-04-01",
            "cost_gbp": 50,
            "description": "Lunch",
            "expense_type": "food"
        }
