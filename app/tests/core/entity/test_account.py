import unittest

from app.src.core.entity.account import Account
from app.src.core.entity.holder import Holder
from app.src.core.exceptions.empty_id_exception import EmptyIdException


class AccountTestCase(unittest.TestCase):

    def setUp(self):
        self._account_id = 'acc67890'
        self._holder = Holder('John Doe', 'john.doe@example.com', '759.520.250-72')

    def test_create_account_obj(self):
        try:
            account = Account(self._account_id, self._holder)
            self.assertEqual(self._account_id, account.id)
            self.assertEqual(self._holder, account.holder)
        except Exception as exp:
            self.assertFalse(exp)

    def test_create_account_with_empty_id(self):
        try:
            Account('   ', self._holder)
        except Exception as exp:
            self.assertRaises(EmptyIdException)

    def test_create_account_with_no_id(self):
        try:
            Account(holder=self._holder)
        except Exception as exp:
            self.assertRaises(EmptyIdException)



if __name__ == '__main__':
    unittest.main()
