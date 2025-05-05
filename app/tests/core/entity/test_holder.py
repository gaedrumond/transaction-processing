import unittest

from app.src.core.entity.holder import Holder
from app.src.core.exceptions.invalid_document_exception import InvalidDocumentException


class HolderTestCase(unittest.TestCase):

    def setUp(self):
        self._name = 'John Doe'
        self._email = 'john.doe@example.com'
        self._cpf = '759.520.250-72'
        self._cnpj = '44.637.385/0001-78'

    def test_create_new_holder_with_cpf(self):
        try:
            holder = Holder(self._name, self._email, self._cpf)
            self.assertEqual(self._name, holder.name)
            self.assertEqual(self._email, holder.email)
            self.assertEqual(self._cpf, holder.document)
            self.assertEqual('cpf', holder.document_type)
        except Exception as exp:
            self.assertFalse(exp)

    def test_create_new_holder_with_cnpj(self):
        try:
            holder = Holder(self._name, self._email, self._cnpj)
            self.assertEqual(self._name, holder.name)
            self.assertEqual(self._email, holder.email)
            self.assertEqual(self._cnpj, holder.document)
            self.assertLogs('cnpj', holder.document_type)
        except Exception as exp:
            self.assertFalse(exp)

    def test_create_new_holder_with_invalid_document(self):
        try:
            Holder(self._name, self._email, '123456789')
        except Exception as exp:
            self.assertRaises(InvalidDocumentException)


    def test_create_new_holder_with_empty_document(self):
        try:
            Holder(self._name, self._email, '       ')
        except Exception as exp:
            self.assertRaises(InvalidDocumentException)


    def test_create_new_holder_with_no_document(self):
        try:
            Holder(self._name, self._email)
        except Exception as exp:
            self.assertRaises(InvalidDocumentException)

if __name__ == '__main__':
    unittest.main()
