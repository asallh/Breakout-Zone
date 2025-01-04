class ModelUtility:

    @classmethod
    def find_key(cls, key, target_dictionary):
        if key in target_dictionary:
            return target_dictionary[key]
        for k, v in target_dictionary.items():
            if isinstance(v, dict):
                item = cls.find_key(key, v)
                if item is not None:
                    return item
        return None