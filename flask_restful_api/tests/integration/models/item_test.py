from flask_restful_api.tests.base_test import BaseTest
from flask_restful_api.resources.item import Item, ItemList
from flask_restful_api.models.item import ItemModel


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))
