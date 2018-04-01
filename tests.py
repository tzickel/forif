from forif import if_exists, if_predicate, if_predicate_each, if_unpack
import unittest


class TestForIf(unittest.TestCase):
    def test_iterate_number(self):
        data = 3
        for p in if_unpack(data):
            raise RuntimeError()
        else:
            pass

    def test_second_item(self):
        data = [1, 2, 3]
        for second in if_predicate(data, lambda x: x[1]):
            self.assertEqual(2, second)
            break
        else:
            raise RuntimeError()

    def test_no_forth_item(self):
        data = [1, 2, 3]
        for forth in if_predicate(data, lambda x: x[3]):
            raise RuntimeError()
            break
        else:
            pass

    def test_unpack_none(self):
        data = None
        for k, v in if_unpack(data, lambda x: x.items()):
            raise RuntimeError()
            break
        else:
            pass

    def test_get_values_with_atleast_4_items(self):
        data = {
            'a': [1, 2, 3, 10],
            'b': [4, 5, 6]
        }
        for k, v in if_unpack(data, lambda x: x.items()):
            for p, q in if_exists(v, lambda x: (x[0], x[3])):
                self.assertEqual(1, p)
                self.assertEqual(10, q)
                break
            else:
                raise RuntimeError()
            break
        else:
            raise RuntimeError()


    def test_complex_data_filter(self):
        data = {
            'items': 2,
            'users': [
                {
                    'name': '1',
                    'address': 'yes'
                },
                {
                    'name': '2',
                    'address': None
                },
                {
                    'name': '3',
                }
            ]
        }
        for user in if_unpack(data, lambda x: x['users']):
            for name, address in if_exists(user, lambda x: (x['name'], x['address'])):
                self.assertTrue((name, address) in [('1', 'yes'), ('2', None)])

    def test_all_members_are_not_none(self):
        data = {
            'items': 2,
            'users': [
                {
                    'name': '1',
                    'address': 'yes'
                },
                {
                    'name': '2',
                    'address': None
                },
                {
                    'name': '3',
                }
            ]
        }
        for user in if_unpack(data, lambda x: x['users']):
            for name, address in if_predicate_each(user, lambda x: (x['name'], x['address'])):
                self.assertEqual((name, address), ('1', 'yes'))


if __name__ == '__main__':
    unittest.main()
