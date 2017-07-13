import unittest
from app.models import User, Bucket


class TestUserBucket(unittest.TestCase):
    def setUp(self):
        self.user = User('jokamjohn', '123')

    def test_user_can_create_bucket(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.assertTrue(self.user.create_bucket(bucket))

    def test_user_bucket_already_exists(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.assertFalse(self.user.create_bucket(bucket))

    def test_a_bucket_is_returned_when_an_id_is_specified(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.assertEqual(self.user.get_bucket("AZXDJSA"), bucket)

    def test_none_is_returned_for_a_bucket_that_does_not_exist(self):
        self.assertIsNone(self.user.get_bucket("ABGDTAD"))