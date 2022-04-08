from odoo import api, fields, models


class Jenis_Buku(models.Model):
    _name = 'book.category'
    _description = 'bookTitle'

    title = fields.Char(string='bookTitle')
    pengarang = fields.Char(string='Nama Pengarang')
    tahun = fields.Integer(string='Tahun Buku')
    jumlah = fields.Integer(string='Jumlah Buku')
    price = fields.Integer(string= 'bookPrice')