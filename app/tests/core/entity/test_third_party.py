import unittest

from app.src.core.entity.third_party import Partner


class PartnerTestCase(unittest.TestCase):

    def setUp(self):
        self._name = "Payment Processor Inc."
        self._email = "support@paymentprocessor.com"

    def test_create_partner_object(self):
        partner = Partner(self._name, self._email)
        self.assertEqual(self._name, partner.name)
        self.assertEqual(self._email, partner.email)

if __name__ == '__main__':
    unittest.main()
