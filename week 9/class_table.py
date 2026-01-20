class ClassSymbol:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.methods = {}
        self.fields = {}

    def add_method(self, name, return_type, params=None):
        self.methods[name] = {"return_type": return_type, "params": params or []}

    def add_field(self, name, field_type):
        self.fields[name] = field_type

    def get_inherited_methods(self):
        """Get methods including inherited from parent"""
        methods = dict(self.methods)
        if self.parent:
            methods.update(self.parent.get_inherited_methods())
        return methods

    def get_inherited_fields(self):
        """Get fields including inherited from parent"""
        fields = dict(self.fields)
        if self.parent:
            fields.update(self.parent.get_inherited_fields())
        return fields


class ClassTable:
    def __init__(self):
        self.classes = {}

    def add_class(self, name, parent=None):
        parent_class = self.classes.get(parent) if parent else None
        self.classes[name] = ClassSymbol(name, parent_class)

    def get_class(self, name):
        return self.classes.get(name)

    def check_inheritance(self, child_name, parent_name):
        """Check if child inherits from parent"""
        child = self.get_class(child_name)
        if not child:
            return False
        current = child.parent
        while current:
            if current.name == parent_name:
                return True
            current = current.parent
        return False
