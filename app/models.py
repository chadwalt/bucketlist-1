class User:
    """
    User model class 
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
        self.buckets = {}

    def create_bucket(self, bucket):
        """
        Create a bucket if it does not exist already
        :param bucket: 
        :return: 
        """
        if bucket.id in self.buckets.keys():
            return False
        else:
            self.buckets[bucket.id] = bucket
            return True

    def update_bucket(self, bucket_id, name):
        """
        This method first checks whether the bucket exists,
        if it does it changes the bucket name to the
        new one
        :param bucket_id: 
        :param name: 
        :return: 
        """
        if bucket_id in self.buckets.keys():
            bucket = self.buckets[bucket_id]
            bucket.name = name
            return True
        return False

    def delete_bucket(self, bucket_id):
        """
        Delete a bucket from the User's bucket if
        it exists.
        :param bucket_id: 
        :return: 
        """
        if bucket_id in self.buckets.keys():
            self.buckets.pop(bucket_id)
            return True
        return False

    def get_buckets(self):
        """
        Get a user's buckets
        :return: 
        """
        return self.buckets

    def get_bucket(self, bucket_id):
        """
        Get a user's bucket by Id
        :param bucket_id: 
        :return: 
        """
        if bucket_id in self.buckets.keys():
            return self.buckets[bucket_id]
        return None


class Bucket:
    """
    Bucket class
    """

    def __init__(self, bucket_id, name):
        self.id = bucket_id
        self.name = name
        self.items = {}

    def create_item(self, item):
        """
        Create a bucket item if it does not already exist
        :param item: 
        :return: 
        """
        if item.id in self.items.keys():
            return False
        else:
            self.items[item.id] = item
            return True

    def get_item(self, item_id):
        """
        Get the item by its Id
        :param item_id: 
        :return: 
        """
        if item_id in self.items.keys():
            return self.items[item_id]
        return None

    def update_item(self, item_id, name, description, deadline):
        """
        Method to update the item in the bucket.
        :param item_id: 
        :param name: 
        :param description: 
        :param deadline: 
        :return: 
        """
        if item_id in self.items.keys():
            item = self.items[item_id]
            item.name = name
            item.description = description
            item.deadline = deadline
            return True
        return False

    def delete_item(self, item_id):
        """
        Delete an item from the bucket.
        :param item_id: 
        :return: 
        """
        if item_id in self.items.keys():
            self.items.pop(item_id)
            return True
        return False


class BucketItem:
    """
    BucketItem class
    """

    def __init__(self, item_id, name, description, deadline):
        self.id = item_id
        self.name = name
        self.description = description
        self.deadline = deadline
