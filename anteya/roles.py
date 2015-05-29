from rolepermissions.roles import AbstractUserRole


class Firm(AbstractUserRole):
    available_permissions = {
        'create_ivoices': True,
    }


class Client(AbstractUserRole):
    available_permissions = {
        'dowload_invoices': True,
    }
